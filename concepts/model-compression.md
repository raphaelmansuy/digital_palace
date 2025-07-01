# 🔧 Model Compression

**Model Compression** involves techniques to reduce the size, memory footprint, and computational requirements of machine learning models while preserving their performance for efficient deployment.

## 🎯 Core Concepts

### **Compression Techniques**

- **Quantization**: Reduce numerical precision (FP32 → INT8/INT4)
- **Pruning**: Remove unnecessary weights and connections
- **Knowledge Distillation**: Train smaller models from larger ones
- **Low-Rank Factorization**: Decompose weight matrices
- **Weight Sharing**: Share parameters across model components

### **Optimization Goals**

- **Model Size**: Reduce storage and memory requirements
- **Inference Speed**: Faster prediction times
- **Energy Efficiency**: Lower power consumption
- **Hardware Compatibility**: Enable deployment on resource-constrained devices

## 🛠️ Popular Tools & Frameworks

### **Quantization Tools**

- **[TensorFlow Model Optimization](https://tensorflow.org/model_optimization)** - Complete optimization toolkit
- **[PyTorch Quantization](https://pytorch.org/docs/stable/quantization.html)** - Native PyTorch quantization
- **[ONNX Quantization](https://onnxruntime.ai/docs/performance/quantization.html)** - ONNX model optimization
- **[Intel Neural Compressor](https://github.com/intel/neural-compressor)** - Intel's optimization toolkit

### **Pruning Libraries**

- **[TensorFlow Model Optimization](https://tensorflow.org/model_optimization/guide/pruning)** - Structured and unstructured pruning
- **[PyTorch Pruning](https://pytorch.org/tutorials/intermediate/pruning_tutorial.html)** - Built-in pruning utilities
- **[Magnitude Pruning](https://github.com/tensorflow/model-optimization)** - Magnitude-based weight removal

### **Knowledge Distillation**

- **[Distiller](https://github.com/NervanaSystems/distiller)** - Neural network distillation library
- **[TinyBERT](https://github.com/huawei-noah/Pretrained-Language-Model/tree/master/TinyBERT)** - BERT distillation
- **[DistilBERT](https://huggingface.co/distilbert-base-uncased)** - Distilled BERT model

## 🏗️ Implementation Examples

### **Post-Training Quantization**

```python
import tensorflow as tf

def quantize_model(model_path, output_path):
    """Convert a trained model to quantized version"""
    
    # Load the model
    model = tf.keras.models.load_model(model_path)
    
    # Create TFLite converter
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Enable quantization
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    
    # Optional: Set representative dataset for calibration
    def representative_dataset():
        for i in range(100):
            # Provide sample input data
            yield [tf.random.normal([1, 224, 224, 3])]
    
    converter.representative_dataset = representative_dataset
    
    # Enable INT8 quantization
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8
    
    # Convert model
    quantized_model = converter.convert()
    
    # Save quantized model
    with open(output_path, 'wb') as f:
        f.write(quantized_model)
    
    # Compare model sizes
    original_size = os.path.getsize(model_path)
    quantized_size = len(quantized_model)
    compression_ratio = original_size / quantized_size
    
    print(f"Original model size: {original_size / 1024 / 1024:.2f} MB")
    print(f"Quantized model size: {quantized_size / 1024 / 1024:.2f} MB")
    print(f"Compression ratio: {compression_ratio:.2f}x")
    
    return quantized_model
```

### **Magnitude-Based Pruning**

```python
import tensorflow as tf
import tensorflow_model_optimization as tfmot

def create_pruned_model(base_model, target_sparsity=0.5):
    """Apply magnitude-based pruning to a model"""
    
    # Define pruning parameters
    pruning_params = {
        'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
            initial_sparsity=0.0,
            final_sparsity=target_sparsity,
            begin_step=0,
            end_step=1000
        )
    }
    
    # Apply pruning to the model
    model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(
        base_model, **pruning_params
    )
    
    # Compile the pruned model
    model_for_pruning.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model_for_pruning

def train_pruned_model(model, train_data, validation_data, epochs=10):
    """Train the pruned model with sparsity updates"""
    
    # Add pruning callbacks
    callbacks = [
        tfmot.sparsity.keras.UpdatePruningStep(),
        tfmot.sparsity.keras.PruningSummaries(log_dir='./logs')
    ]
    
    # Train the model
    history = model.fit(
        train_data,
        epochs=epochs,
        validation_data=validation_data,
        callbacks=callbacks
    )
    
    # Remove pruning wrappers and export final model
    final_model = tfmot.sparsity.keras.strip_pruning(model)
    
    return final_model, history

# Example usage
base_model = tf.keras.applications.MobileNetV2(
    weights='imagenet',
    include_top=True,
    classes=1000
)

pruned_model = create_pruned_model(base_model, target_sparsity=0.7)
```

### **Knowledge Distillation**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DistillationLoss(nn.Module):
    """Knowledge distillation loss function"""
    
    def __init__(self, temperature=3.0, alpha=0.7):
        super(DistillationLoss, self).__init__()
        self.temperature = temperature
        self.alpha = alpha
        self.kl_div = nn.KLDivLoss(reduction='batchmean')
        self.ce_loss = nn.CrossEntropyLoss()
    
    def forward(self, student_logits, teacher_logits, labels):
        # Distillation loss (soft targets)
        soft_targets = F.softmax(teacher_logits / self.temperature, dim=1)
        soft_student = F.log_softmax(student_logits / self.temperature, dim=1)
        distillation_loss = self.kl_div(soft_student, soft_targets) * (self.temperature ** 2)
        
        # Standard classification loss (hard targets)
        classification_loss = self.ce_loss(student_logits, labels)
        
        # Combined loss
        total_loss = (
            self.alpha * distillation_loss + 
            (1 - self.alpha) * classification_loss
        )
        
        return total_loss

class StudentModel(nn.Module):
    """Smaller student model"""
    
    def __init__(self, num_classes=1000):
        super(StudentModel, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        self.classifier = nn.Linear(64, num_classes)
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

def train_student_model(teacher_model, student_model, train_loader, epochs=10):
    """Train student model using knowledge distillation"""
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    teacher_model.to(device)
    student_model.to(device)
    
    # Set teacher to evaluation mode
    teacher_model.eval()
    student_model.train()
    
    optimizer = torch.optim.Adam(student_model.parameters(), lr=0.001)
    distillation_loss = DistillationLoss()
    
    for epoch in range(epochs):
        total_loss = 0.0
        
        for batch_idx, (data, labels) in enumerate(train_loader):
            data, labels = data.to(device), labels.to(device)
            
            # Forward pass through both models
            with torch.no_grad():
                teacher_logits = teacher_model(data)
            
            student_logits = student_model(data)
            
            # Calculate distillation loss
            loss = distillation_loss(student_logits, teacher_logits, labels)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {avg_loss:.4f}')
    
    return student_model
```

### **Dynamic Quantization with PyTorch**

```python
import torch
import torch.quantization as quantization

def dynamic_quantize_model(model, example_input):
    """Apply dynamic quantization to a PyTorch model"""
    
    # Set model to evaluation mode
    model.eval()
    
    # Apply dynamic quantization
    quantized_model = torch.quantization.quantize_dynamic(
        model,
        {torch.nn.Linear, torch.nn.Conv2d},  # Layers to quantize
        dtype=torch.qint8
    )
    
    # Compare model sizes
    def get_model_size(model):
        torch.save(model.state_dict(), "temp.p")
        size = os.path.getsize("temp.p")
        os.remove("temp.p")
        return size
    
    original_size = get_model_size(model)
    quantized_size = get_model_size(quantized_model)
    
    print(f"Original model size: {original_size / 1024 / 1024:.2f} MB")
    print(f"Quantized model size: {quantized_size / 1024 / 1024:.2f} MB")
    print(f"Size reduction: {(1 - quantized_size/original_size) * 100:.1f}%")
    
    # Compare inference times
    def measure_inference_time(model, input_tensor, num_runs=100):
        import time
        model.eval()
        
        with torch.no_grad():
            # Warmup
            for _ in range(10):
                _ = model(input_tensor)
            
            # Measure
            start_time = time.time()
            for _ in range(num_runs):
                _ = model(input_tensor)
            end_time = time.time()
        
        return (end_time - start_time) / num_runs
    
    original_time = measure_inference_time(model, example_input)
    quantized_time = measure_inference_time(quantized_model, example_input)
    
    print(f"Original inference time: {original_time * 1000:.2f} ms")
    print(f"Quantized inference time: {quantized_time * 1000:.2f} ms")
    print(f"Speedup: {original_time / quantized_time:.2f}x")
    
    return quantized_model
```

## 📊 Compression Strategies

### **Model Size vs. Accuracy Trade-offs**

- Start with post-training quantization (easiest)
- Apply pruning for further size reduction
- Use knowledge distillation for maintaining accuracy
- Combine techniques for maximum compression

### **Hardware-Specific Optimization**

- **Mobile/Edge**: Prioritize model size and energy efficiency
- **Cloud/Server**: Focus on throughput and batch processing
- **IoT**: Extreme compression with acceptable accuracy loss
- **Real-time**: Balance latency and accuracy

### **Evaluation Metrics**

- Model accuracy degradation
- Inference latency improvement
- Memory usage reduction
- Energy consumption decrease
- Hardware utilization efficiency

## 🔗 Integration with Other Concepts

- **[Edge AI & Mobile AI](./edge-ai.md)** - Essential for mobile deployment
- **[Inference](./inference.md)** - Optimized inference strategies
- **[Real-time AI](./real-time-ai.md)** - Low-latency requirements
- **[Production Deployment](./production-deployment.md)** - Deployment optimization
- **[MLOps](./mlops.md)** - Automated optimization pipelines

## 📚 Learning Resources

### **Courses & Tutorials**

- [TensorFlow Model Optimization Guide](https://tensorflow.org/model_optimization)
- [PyTorch Quantization Tutorial](https://pytorch.org/tutorials/advanced/static_quantization_tutorial.html)
- [MIT 6.5940: TinyML and Efficient Deep Learning](https://efficientml.ai/)

### **Research Papers**

- "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"
- "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
- "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"

### **Books**

- "Efficient Deep Learning" by Gaurav Menghani
- "TinyML: Machine Learning with TensorFlow Lite" by Pete Warden

---

**🔗 Navigation**
- [← Back to Concepts Hub](./README.md)
- [Edge AI & Mobile AI →](./edge-ai.md)
- [Inference →](./inference.md)
