# 🗺️ Knowledge Graphs

**Knowledge Graphs** are structured representations of information that model relationships between entities, enabling machines to understand and reason about complex interconnected data.

## 🎯 Core Concepts

### **Graph Fundamentals**

- **Entities**: Real-world objects, concepts, or things (nodes)
- **Relationships**: Connections between entities (edges)
- **Properties**: Attributes that describe entities and relationships
- **Schema**: Structure defining entity types and relationship patterns

### **Knowledge Representation**

- **RDF (Resource Description Framework)**: Standard for representing information
- **Ontologies**: Formal specifications of concepts and relationships
- **Semantic Web**: Web of linked data using standardized formats
- **Graph Databases**: Specialized databases for storing and querying graphs

### **Reasoning & Inference**

- **Logical Reasoning**: Derive new facts from existing knowledge
- **Graph Neural Networks**: ML models that operate on graph structures
- **Link Prediction**: Predict missing relationships in graphs
- **Entity Resolution**: Identify and merge duplicate entities

## 🛠️ Popular Tools & Platforms

### **Graph Databases**

- **[Neo4j](https://neo4j.com/)** - Leading graph database platform
- **[Amazon Neptune](https://aws.amazon.com/neptune/)** - Fully managed graph database
- **[ArangoDB](https://www.arangodb.com/)** - Multi-model database with graph support
- **[TigerGraph](https://www.tigergraph.com/)** - Scalable graph analytics platform

### **Knowledge Graph Frameworks**

- **[Apache Jena](https://jena.apache.org/)** - Java framework for semantic web applications
- **[RDFLib](https://rdflib.readthedocs.io/)** - Python library for working with RDF
- **[Stardog](https://www.stardog.com/)** - Enterprise knowledge graph platform
- **[GraphDB](https://graphdb.ontotext.com/)** - RDF database and SPARQL endpoint

### **Graph ML Libraries**

- **[PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)** - Graph neural networks in PyTorch
- **[DGL (Deep Graph Library)](https://www.dgl.ai/)** - Python package for deep learning on graphs
- **[NetworkX](https://networkx.org/)** - Python package for complex networks
- **[Spektral](https://graphneural.network/)** - Graph neural networks in TensorFlow/Keras

### **Knowledge Extraction Tools**

- **[spaCy](https://spacy.io/)** - NLP library with entity recognition
- **[Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/)** - NLP toolkit with relation extraction
- **[OpenIE](https://github.com/dair-iitd/OpenIE-standalone)** - Open information extraction
- **[REBEL](https://github.com/Babelscape/rebel)** - Relation extraction for building knowledge graphs

## 🏗️ Implementation Examples

### **Building a Simple Knowledge Graph**

```python
import networkx as nx
from rdflib import Graph, Namespace, RDF, RDFS, Literal

class SimpleKnowledgeGraph:
    def __init__(self):
        self.graph = Graph()
        self.ex = Namespace("http://example.org/")
        
    def add_entity(self, entity_id, entity_type, properties=None):
        """Add an entity to the knowledge graph"""
        entity_uri = self.ex[entity_id]
        self.graph.add((entity_uri, RDF.type, self.ex[entity_type]))
        
        if properties:
            for prop, value in properties.items():
                if isinstance(value, str):
                    self.graph.add((entity_uri, self.ex[prop], Literal(value)))
                else:
                    self.graph.add((entity_uri, self.ex[prop], self.ex[str(value)]))
    
    def add_relationship(self, subject, predicate, object):
        """Add a relationship between entities"""
        self.graph.add((self.ex[subject], self.ex[predicate], self.ex[object]))
    
    def query(self, sparql_query):
        """Execute SPARQL query on the knowledge graph"""
        return self.graph.query(sparql_query)
    
    def export_to_file(self, filename, format="turtle"):
        """Export knowledge graph to file"""
        self.graph.serialize(destination=filename, format=format)

# Example usage
kg = SimpleKnowledgeGraph()

# Add entities
kg.add_entity("john_doe", "Person", {"name": "John Doe", "age": 30})
kg.add_entity("company_a", "Company", {"name": "Company A"})
kg.add_entity("software_engineer", "JobTitle")

# Add relationships
kg.add_relationship("john_doe", "worksFor", "company_a")
kg.add_relationship("john_doe", "hasJobTitle", "software_engineer")
```

### **Neo4j Integration Example**

```python
from neo4j import GraphDatabase

class Neo4jKnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def create_person(self, name, age, occupation):
        """Create a person node"""
        with self.driver.session() as session:
            session.write_transaction(self._create_person, name, age, occupation)
    
    @staticmethod
    def _create_person(tx, name, age, occupation):
        query = """
        CREATE (p:Person {name: $name, age: $age, occupation: $occupation})
        RETURN p
        """
        return tx.run(query, name=name, age=age, occupation=occupation)
    
    def create_relationship(self, person1, person2, relationship_type):
        """Create relationship between two people"""
        with self.driver.session() as session:
            session.write_transaction(
                self._create_relationship, person1, person2, relationship_type
            )
    
    @staticmethod
    def _create_relationship(tx, person1, person2, relationship_type):
        query = f"""
        MATCH (p1:Person {{name: $person1}})
        MATCH (p2:Person {{name: $person2}})
        CREATE (p1)-[:{relationship_type}]->(p2)
        """
        return tx.run(query, person1=person1, person2=person2)
    
    def find_connections(self, person_name):
        """Find all connections for a person"""
        with self.driver.session() as session:
            return session.read_transaction(self._find_connections, person_name)
    
    @staticmethod
    def _find_connections(tx, person_name):
        query = """
        MATCH (p:Person {name: $person_name})-[r]-(connected)
        RETURN connected.name AS name, type(r) AS relationship
        """
        return [record for record in tx.run(query, person_name=person_name)]
```

### **Knowledge Graph for RAG Enhancement**

```python
import openai
from sentence_transformers import SentenceTransformer

class KnowledgeGraphRAG:
    def __init__(self, kg_database, embedding_model="all-MiniLM-L6-v2"):
        self.kg = kg_database
        self.embedding_model = SentenceTransformer(embedding_model)
        
    def extract_entities(self, text):
        """Extract entities from text using NLP"""
        # Using spaCy for entity extraction
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        
        entities = []
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            })
        return entities
    
    def find_related_entities(self, entity, max_hops=2):
        """Find entities related to given entity within max_hops"""
        query = f"""
        MATCH (start:Entity {{name: '{entity}'}})-[*1..{max_hops}]-(related)
        RETURN DISTINCT related.name AS name, related.type AS type
        LIMIT 20
        """
        return self.kg.query(query)
    
    def enhance_query_with_kg(self, user_query):
        """Enhance user query with knowledge graph context"""
        # Extract entities from user query
        entities = self.extract_entities(user_query)
        
        # Find related entities in knowledge graph
        context_entities = []
        for entity in entities:
            related = self.find_related_entities(entity["text"])
            context_entities.extend(related)
        
        # Build enhanced context
        context = f"Query: {user_query}\n"
        context += "Related entities from knowledge graph:\n"
        for entity in context_entities[:10]:  # Limit context
            context += f"- {entity['name']} (type: {entity['type']})\n"
        
        return context
    
    def generate_answer(self, user_query):
        """Generate answer using knowledge graph enhanced RAG"""
        enhanced_query = self.enhance_query_with_kg(user_query)
        
        # Use enhanced query with LLM
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant with access to a knowledge graph. Use the provided context to answer questions accurately."},
                {"role": "user", "content": enhanced_query}
            ]
        )
        
        return response.choices[0].message.content
```

### **Graph Neural Network Example**

```python
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data

class SimpleGNN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleGNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)
        
    def forward(self, x, edge_index):
        # First graph convolution layer
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        
        # Second graph convolution layer
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Example usage for node classification
def train_gnn_on_knowledge_graph():
    # Create graph data (example)
    x = torch.randn(100, 16)  # 100 nodes with 16 features each
    edge_index = torch.randint(0, 100, (2, 300))  # 300 edges
    y = torch.randint(0, 7, (100,))  # 7 classes
    
    data = Data(x=x, edge_index=edge_index, y=y)
    
    # Initialize model
    model = SimpleGNN(input_dim=16, hidden_dim=32, output_dim=7)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    # Training loop
    model.train()
    for epoch in range(200):
        optimizer.zero_grad()
        out = model(data.x, data.edge_index)
        loss = F.nll_loss(out, data.y)
        loss.backward()
        optimizer.step()
        
        if epoch % 50 == 0:
            print(f'Epoch {epoch}, Loss: {loss.item():.4f}')
    
    return model
```

## 📊 Use Cases & Applications

### **Enhanced RAG Systems**

- Structured knowledge retrieval
- Multi-hop reasoning
- Context-aware answer generation
- Fact verification

### **Recommendation Systems**

- Content-based recommendations
- Collaborative filtering with graphs
- Explainable recommendations
- Cold start problem mitigation

### **Enterprise Knowledge Management**

- Document and expertise mapping
- Organizational knowledge discovery
- Compliance and governance
- Semantic search

### **AI Agents & Automation**

- Planning and decision making
- Multi-agent coordination
- Workflow automation
- Resource allocation

## 🔗 Integration with Other Concepts

- **[RAG](./rag.md)** - Knowledge graphs enhance retrieval systems
- **[Knowledge Management](./knowledge-management.md)** - Structured knowledge organization
- **[AI Agents](./ai-agents.md)** - Agents using structured knowledge for reasoning
- **[Datasets](./datasets.md)** - Graph datasets for training and evaluation
- **[Embeddings](./embeddings.md)** - Vector representations of graph entities

## 📚 Learning Resources

### **Courses & Tutorials**

- [Knowledge Graphs Course (Stanford)](https://web.stanford.edu/class/cs520/)
- [Graph Neural Networks Course](https://distill.pub/2021/gnn-intro/)
- [Neo4j Graph Academy](https://graphacademy.neo4j.com/)

### **Books**

- "Knowledge Graphs: Fundamentals, Techniques, and Applications" by Mayank Kejriwal
- "Graph Databases" by Ian Robinson and Jim Webber
- "Learning with Graphs" by Mikhail Belkin

### **Research Papers**

- "A Comprehensive Survey on Graph Neural Networks" (Wu et al., 2020)
- "Knowledge Graphs" (Hogan et al., 2021)
- "Graph Attention Networks" (Veličković et al., 2018)

---

**🔗 Navigation**
- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [Knowledge Management →](./knowledge-management.md)
