# 🔍 RAG & Knowledge Systems

> Build AI that understands and works with your own data

## 🎯 What You'll Build

By the end of this guide, you'll have:
- ✅ AI that answers questions using your documents
- ✅ Knowledge extraction from PDFs, websites, and databases
- ✅ Semantic search across your data
- ✅ Real-time knowledge updates

## 🚀 Quick Start (45 minutes)

### Step 1: Simple Document Q&A

```python
# Install essentials
pip install langchain chromadb pypdf

# Basic RAG system
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load and split documents
loader = PyPDFLoader("your-document.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(documents)

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(splits, embeddings)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever()
)

# Ask questions!
response = qa_chain.run("What are the main points in this document?")
print(response)
```

**Success Check**: You can ask questions about your PDF ✅

---

## 🏗️ RAG Architecture Patterns

### Pattern 1: Simple RAG
```
Documents → Embeddings → Vector Store → Retrieval → LLM → Answer
```
**Best for**: Single domain, static documents

### Pattern 2: Advanced RAG
```
Documents → Processing → Multi-Store → Hybrid Retrieval → Reranking → LLM → Answer
```
**Best for**: Large document collections, better accuracy

### Pattern 3: Agentic RAG
```
Question → Planning → Tool Selection → Retrieval → Synthesis → Verification → Answer
```
**Best for**: Complex queries, multiple data sources

### Pattern 4: Graph RAG
```
Documents → Entity Extraction → Knowledge Graph → Graph Traversal → LLM → Answer
```
**Best for**: Connected knowledge, relationship queries

---

## 🛠️ Essential Components

### Document Processing

#### **Text Extraction**
| Tool | Best For | Accuracy |
|------|----------|----------|
| [Docling](https://docling-project.github.io/docling/) | Advanced parsing, multimodal, RAG integrations | ⭐ Excellent |
| [PyPDF2](https://github.com/py-pdf/PyPDF2) | Simple PDFs | 🟡 Medium |
| [pdfplumber](https://github.com/jsvine/pdfplumber) | Complex layouts | 🟢 High |
| [zerox](https://github.com/getomni-ai/zerox) | OCR + Vision models | ⭐ Excellent |
| [unstructured](https://github.com/Unstructured-IO/unstructured) | Multiple formats | 🟢 High |

#### **Text Chunking Strategies**
```python
# Strategy 1: Fixed size (simple)
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Strategy 2: Recursive (recommended)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

# Strategy 3: Semantic (advanced)
from langchain.text_splitter import SemanticChunker
text_splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile"
)
```


### Vector Databases

#### **Local Development**
| Database | Setup | Best For |
|----------|-------|----------|
| **[Chroma](https://github.com/chroma-core/chroma)** | `pip install chromadb` | Prototyping |
| **[FAISS](https://github.com/facebookresearch/faiss)** | `pip install faiss-cpu` | Fast similarity search |
| **[Qdrant](https://qdrant.tech/)** | Docker or cloud | Production-ready |

#### **Production Scale**
| Database | Strengths | Use Case |
|----------|-----------|----------|
| **[Pinecone](https://www.pinecone.io/)** | Managed, scalable | Enterprise |
| **[Weaviate](https://weaviate.io/)** | Open source, flexible | Custom deployments |
| **[pgvectorscale](https://github.com/timescale/pgvectorscale/)** | PostgreSQL-based | Existing PostgreSQL setups |
| **[PGVector CloudSQL GCP](https://github.com/sciences44/pgvector_cloudsql_gcp)** | Infrastructure-as-Code PostgreSQL with PGVector on Google Cloud SQL | Production-ready GCP deployments |

**Advanced Example:**

- **[Hands-on Multi-Vector Retrieval with Reason-ModernColBERT in Weaviate (LightOn)](https://github.com/weaviate/recipes/blob/main/weaviate-features/multi-vector/reason_moderncolbert.ipynb)**  
  Step-by-step notebook: advanced RAG with multi-vector embeddings and late interaction retrieval using Reason-ModernColBERT in Weaviate. Covers setup, code, and reasoning-intensive search for agentic RAG and production use cases.

### Embedding Models

#### **General Purpose**
```python
# OpenAI (paid, high quality)
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Sentence Transformers (free, good quality)
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Ollama (local, private)
from langchain.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
```

#### **Specialized Models**
- **Code**: `microsoft/codebert-base`
- **Legal**: `nlpaueb/legal-bert-base-uncased`
- **Medical**: `emilyalsentzer/Bio_ClinicalBERT`
- **Multilingual**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

---

## 🎨 Advanced RAG Techniques

### 1. Hybrid Retrieval

```python
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever

# Combine vector and keyword search
vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
bm25_retriever = BM25Retriever.from_documents(documents)

ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.7, 0.3]  # Favor vector search
)
```

### 2. Query Rewriting

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

query_rewrite_template = """
Original query: {query}

Rewrite this query to be more specific and likely to find relevant documents.
Consider:
- Adding context clues
- Breaking down complex questions
- Using domain-specific terminology

Rewritten query:
"""

query_rewriter = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(query_rewrite_template)
)

def enhanced_retrieval(query):
    rewritten_query = query_rewriter.run(query=query)
    return retriever.get_relevant_documents(rewritten_query)
```

### 3. Re-ranking Results

```python
from langchain.document_transformers import LongContextReorder

# Reorder documents for better context
reordering = LongContextReorder()

def rerank_documents(query, documents):
    # Score documents by relevance
    scored_docs = []
    for doc in documents:
        relevance_score = calculate_relevance(query, doc.page_content)
        scored_docs.append((doc, relevance_score))
    
    # Sort by score and reorder for context
    sorted_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    top_docs = [doc for doc, score in sorted_docs[:5]]
    
    return reordering.transform_documents(top_docs)
```

### 4. Multi-Document Synthesis

```python
class MultiDocumentRAG:
    def __init__(self, vector_stores: dict):
        self.vector_stores = vector_stores
        self.llm = ChatOpenAI()
    
    def query_multiple_sources(self, query: str) -> str:
        all_results = {}
        
        # Query each source
        for source_name, store in self.vector_stores.items():
            docs = store.similarity_search(query, k=3)
            all_results[source_name] = docs
        
        # Synthesize results
        synthesis_prompt = f"""
        Query: {query}
        
        Information from multiple sources:
        {self._format_sources(all_results)}
        
        Provide a comprehensive answer that:
        1. Synthesizes information from all sources
        2. Notes any contradictions
        3. Cites which sources support each point
        """
        
        return self.llm.predict(synthesis_prompt)
```

#### Further Reading
- **[Integrating Long-Term Memory with Gemini 2.5 (Philipp Schmid)](https://www.philschmid.de/gemini-with-memory)** — Practical walkthrough of adding persistent memory to Gemini-based chatbots using Mem0 and vector search.

---

## 🔗 Knowledge Graph Integration

### Building Knowledge Graphs

#### **With LightRAG**
```python
from lightrag import LightRAG

# Initialize with knowledge graph capabilities
rag = LightRAG(
    working_dir="./knowledge_graph",
    llm_model_func=your_llm_func,
    embedding_func=your_embedding_func
)

# Insert documents (automatically builds graph)
rag.insert("Your document content here")

# Query with graph traversal
response = rag.query(
    "What are the relationships between concept A and B?",
    param=QueryParam(mode="hybrid")  # Uses both vector and graph
)
```

#### **Custom Graph Construction**
```python
import networkx as nx
from langchain.chains import GraphQAChain

class DocumentGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.entity_extractor = self._setup_entity_extractor()
    
    def add_document(self, doc_content: str, doc_id: str):
        # Extract entities and relationships
        entities = self.entity_extractor.extract_entities(doc_content)
        relationships = self.entity_extractor.extract_relationships(doc_content)
        
        # Add to graph
        for entity in entities:
            self.graph.add_node(entity, document=doc_id)
        
        for rel in relationships:
            self.graph.add_edge(rel.source, rel.target, 
                               relationship=rel.type, document=doc_id)
    
    def find_connected_concepts(self, concept: str, max_distance: int = 2):
        if concept not in self.graph:
            return []
        
        connected = nx.single_source_shortest_path_length(
            self.graph, concept, cutoff=max_distance
        )
        return list(connected.keys())
```

---

## 📊 Data Source Integration

### Web Content

#### **Website Crawling**
```python
from langchain.document_loaders import FireCrawlLoader

# Crawl and convert websites
loader = FireCrawlLoader(
    api_key="your-firecrawl-key",
    url="https://example.com",
    mode="crawl",
    params={
        "crawlerOptions": {
            "includes": ["docs/*"],
            "limit": 100
        }
    }
)

documents = loader.load()
```

#### **API Integration**
```python
class APIDataLoader:
    def __init__(self, api_endpoint, headers=None):
        self.endpoint = api_endpoint
        self.headers = headers or {}
    
    def load_and_process(self):
        response = requests.get(self.endpoint, headers=self.headers)
        data = response.json()
        
        # Convert API response to documents
        documents = []
        for item in data:
            doc = Document(
                page_content=self._format_content(item),
                metadata={
                    "source": "api",
                    "id": item.get("id"),
                    "timestamp": datetime.now().isoformat()
                }
            )
            documents.append(doc)
        
        return documents
```

### Database Integration

#### **SQL Databases**
```python
from langchain.document_loaders import SQLDatabaseLoader

# Load from database
loader = SQLDatabaseLoader(
    query="SELECT content, metadata FROM documents WHERE category='AI'",
    db=your_database_connection
)

documents = loader.load()
```

#### **NoSQL/Document Stores**
```python
class MongoDBLoader:
    def __init__(self, connection_string, database, collection):
        self.client = MongoClient(connection_string)
        self.db = self.client[database]
        self.collection = self.db[collection]
    
    def load_documents(self, query=None):
        query = query or {}
        documents = []
        
        for doc in self.collection.find(query):
            documents.append(Document(
                page_content=doc.get("content", ""),
                metadata={
                    "source": "mongodb",
                    "_id": str(doc["_id"]),
                    **{k: v for k, v in doc.items() if k != "content"}
                }
            ))
        
        return documents
```

---

## 🚀 Production-Ready RAG Systems

### Scalable Architecture

```python
class ProductionRAG:
    def __init__(self):
        self.vector_store = self._setup_vector_store()
        self.llm = self._setup_llm()
        self.cache = self._setup_cache()
        self.monitoring = self._setup_monitoring()
    
    async def query(self, question: str, user_id: str = None) -> dict:
        # Check cache first
        cache_key = hashlib.md5(question.encode()).hexdigest()
        cached_result = await self.cache.get(cache_key)
        if cached_result:
            self.monitoring.log_cache_hit(user_id)
            return cached_result
        
        # Retrieve relevant documents
        start_time = time.time()
        documents = await self._retrieve_documents(question)
        retrieval_time = time.time() - start_time
        
        # Generate answer
        start_time = time.time()
        answer = await self._generate_answer(question, documents)
        generation_time = time.time() - start_time
        
        # Prepare response
        response = {
            "answer": answer,
            "sources": [doc.metadata for doc in documents],
            "retrieval_time": retrieval_time,
            "generation_time": generation_time
        }
        
        # Cache and monitor
        await self.cache.set(cache_key, response, expire=3600)
        self.monitoring.log_query(user_id, question, response)
        
        return response
```

### Real-time Updates

```python
class RealTimeRAG:
    def __init__(self):
        self.vector_store = Qdrant(...)
        self.document_queue = asyncio.Queue()
        self.update_lock = asyncio.Lock()
    
    async def add_document(self, document: Document):
        """Add new document and update index"""
        async with self.update_lock:
            # Process document
            chunks = self.text_splitter.split_documents([document])
            
            # Add to vector store
            for chunk in chunks:
                await self.vector_store.aadd_documents([chunk])
            
            # Update metadata
            self.document_metadata[document.metadata["id"]] = {
                "added_at": datetime.now(),
                "chunk_count": len(chunks)
            }
    
    async def remove_document(self, document_id: str):
        """Remove document from index"""
        async with self.update_lock:
            # Remove from vector store
            await self.vector_store.adelete(
                filter={"document_id": document_id}
            )
            
            # Update metadata
            del self.document_metadata[document_id]
```

---


## 📈 Performance Optimization

> **2025 Perspective: Beyond RAG for Coding Agents**
>
> 🚀 **The landscape is shifting:** While RAG architectures remain powerful for knowledge retrieval, leading teams in 2025 are achieving dramatic performance gains for coding agents by moving beyond RAG. Instead of embedding search and complex retrieval, they leverage direct tool access, sequential file reading, and progressive summarization.
>
> **Key Framework:**
> 1. **Sequential File Reading**: Let agents read files in full, preserving narrative integrity and enabling organic exploration of codebases.
> 2. **Plan First, Act Second**: Separate planning from execution—gather all context before acting, reducing mid-task distractions.
> 3. **Direct Tool Access**: Equip agents with terminal commands, file readers, and code definitions—skip preprocessing layers.
> 4. **Progressive Summarization**: For long tasks, use detailed progress summaries instead of complex truncation.
>
> **Evidence:**
> - [Stanford AI Index 2025](https://aiindex.stanford.edu/report/) shows agents excel in short-horizon tasks, but humans still outperform in longer, complex workflows.
> - Research indicates that larger context windows alone do not solve complex reasoning—direct approaches are often more effective for coding agents.
>
> **Read the full analysis and see the professional Mermaid diagram:**
> [How to 10x your coding agent performance (without RAG)](../personal/linkedin/2025-07-10-no-need-rag.md)


### Retrieval Optimization

```python
class OptimizedRetriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.query_cache = TTLCache(maxsize=1000, ttl=300)
    
    @lru_cache(maxsize=100)
    def get_embeddings(self, query: str):
        """Cache embeddings for repeated queries"""
        return self.embedding_model.embed_query(query)
    
    async def retrieve_with_filters(self, query: str, filters: dict = None):
        """Optimized retrieval with filters"""
        cache_key = (query, frozenset(filters.items()) if filters else None)
        
        if cache_key in self.query_cache:
            return self.query_cache[cache_key]
        
        # Pre-filter documents
        if filters:
            filtered_docs = await self.vector_store.asimilarity_search(
                query,
                k=20,  # Get more initially
                filter=filters
            )
        else:
            filtered_docs = await self.vector_store.asimilarity_search(query, k=10)
        
        # Re-rank by relevance
        reranked_docs = self._rerank_documents(query, filtered_docs)
        
        self.query_cache[cache_key] = reranked_docs[:5]
        return reranked_docs[:5]
```

### Memory Management

```python
class MemoryEfficientRAG:
    def __init__(self, max_memory_mb: int = 1000):
        self.max_memory = max_memory_mb * 1024 * 1024
        self.document_cache = {}
        self.access_times = {}
    
    def _check_memory_usage(self):
        """Evict least recently used documents if memory limit exceeded"""
        current_memory = sum(
            sys.getsizeof(doc) for doc in self.document_cache.values()
        )
        
        if current_memory > self.max_memory:
            # Sort by access time and remove oldest
            sorted_docs = sorted(
                self.access_times.items(),
                key=lambda x: x[1]
            )
            
            for doc_id, _ in sorted_docs:
                if current_memory <= self.max_memory * 0.8:
                    break
                del self.document_cache[doc_id]
                del self.access_times[doc_id]
                current_memory -= sys.getsizeof(self.document_cache.get(doc_id, ""))
```

---

## 🔍 Evaluation & Testing

### Retrieval Quality Metrics

```python
class RAGEvaluator:
    def __init__(self, ground_truth_qa_pairs):
        self.qa_pairs = ground_truth_qa_pairs
        self.llm = ChatOpenAI()
    
    def evaluate_retrieval(self, retriever) -> dict:
        """Evaluate retrieval quality"""
        precision_scores = []
        recall_scores = []
        
        for qa_pair in self.qa_pairs:
            question = qa_pair["question"]
            expected_docs = qa_pair["relevant_documents"]
            
            retrieved_docs = retriever.get_relevant_documents(question)
            retrieved_ids = {doc.metadata["id"] for doc in retrieved_docs}
            expected_ids = set(expected_docs)
            
            # Calculate precision and recall
            intersection = retrieved_ids.intersection(expected_ids)
            precision = len(intersection) / len(retrieved_ids) if retrieved_ids else 0
            recall = len(intersection) / len(expected_ids) if expected_ids else 0
            
            precision_scores.append(precision)
            recall_scores.append(recall)
        
        return {
            "precision": np.mean(precision_scores),
            "recall": np.mean(recall_scores),
            "f1": 2 * np.mean(precision_scores) * np.mean(recall_scores) / 
                  (np.mean(precision_scores) + np.mean(recall_scores))
        }
    
    def evaluate_answer_quality(self, rag_system) -> dict:
        """Evaluate answer quality using LLM-as-judge"""
        scores = []
        
        for qa_pair in self.qa_pairs:
            question = qa_pair["question"]
            expected_answer = qa_pair["answer"]
            
            generated_answer = rag_system.query(question)["answer"]
            
            # Use LLM to score answer quality
            score_prompt = f"""
            Question: {question}
            Expected Answer: {expected_answer}
            Generated Answer: {generated_answer}
            
            Rate the generated answer on a scale of 1-5 for:
            1. Accuracy
            2. Completeness
            3. Relevance
            
            Return only a JSON object with the scores.
            """
            
            score_response = self.llm.predict(score_prompt)
            try:
                scores.append(json.loads(score_response))
            except:
                # Fallback scoring
                scores.append({"accuracy": 3, "completeness": 3, "relevance": 3})
        
        return {
            "avg_accuracy": np.mean([s["accuracy"] for s in scores]),
            "avg_completeness": np.mean([s["completeness"] for s in scores]),
            "avg_relevance": np.mean([s["relevance"] for s in scores])
        }
```

---

## 🎯 Use Case Examples

### 1. Customer Support Knowledge Base

```python
class CustomerSupportRAG:
    def __init__(self):
        self.setup_knowledge_base()
        self.ticket_classifier = self.setup_classifier()
    
    def setup_knowledge_base(self):
        # Load FAQs, manuals, and past tickets
        loaders = [
            CSVLoader("faqs.csv"),
            PyPDFDirectoryLoader("manuals/"),
            JSONLoader("resolved_tickets.json")
        ]
        
        documents = []
        for loader in loaders:
            documents.extend(loader.load())
        
        # Create specialized vector store
        self.vector_store = Chroma.from_documents(
            documents,
            OpenAIEmbeddings(),
            collection_name="customer_support"
        )
    
    def handle_query(self, customer_query: str, customer_info: dict) -> dict:
        # Classify query type
        query_type = self.ticket_classifier.classify(customer_query)
        
        # Retrieve relevant information
        if query_type == "technical":
            retriever = self.vector_store.as_retriever(
                search_kwargs={"filter": {"type": "manual"}}
            )
        else:
            retriever = self.vector_store.as_retriever()
        
        relevant_docs = retriever.get_relevant_documents(customer_query)
        
        # Generate personalized response
        response_prompt = f"""
        Customer Query: {customer_query}
        Customer Tier: {customer_info.get('tier', 'standard')}
        Previous Issues: {customer_info.get('previous_issues', [])}
        
        Relevant Information:
        {self._format_documents(relevant_docs)}
        
        Generate a helpful response that:
        1. Directly addresses the customer's question
        2. Provides step-by-step instructions if applicable
        3. Includes relevant links or documentation
        4. Suggests escalation if needed
        """
        
        return {
            "response": self.llm.predict(response_prompt),
            "confidence": self._calculate_confidence(relevant_docs),
            "suggested_escalation": query_type in ["complex", "billing"],
            "related_articles": [doc.metadata for doc in relevant_docs]
        }
```

### 2. Legal Document Analysis

```python
class LegalRAG:
    def __init__(self):
        self.legal_embeddings = HuggingFaceEmbeddings(
            model_name="nlpaueb/legal-bert-base-uncased"
        )
        self.setup_legal_knowledge_base()
    
    def analyze_contract(self, contract_text: str) -> dict:
        # Extract key clauses
        clauses = self.extract_clauses(contract_text)
        
        analysis_results = {}
        
        for clause_type, clause_text in clauses.items():
            # Find similar clauses in knowledge base
            similar_clauses = self.vector_store.similarity_search(
                clause_text,
                filter={"clause_type": clause_type},
                k=5
            )
            
            # Analyze risks and recommendations
            analysis_prompt = f"""
            Clause Type: {clause_type}
            Clause Text: {clause_text}
            
            Similar Clauses from Database:
            {self._format_clauses(similar_clauses)}
            
            Provide analysis including:
            1. Potential risks
            2. Standard market terms comparison
            3. Recommended modifications
            4. Risk level (Low/Medium/High)
            """
            
            analysis_results[clause_type] = {
                "analysis": self.llm.predict(analysis_prompt),
                "similar_precedents": similar_clauses,
                "risk_score": self._calculate_risk_score(clause_text, similar_clauses)
            }
        
        return analysis_results
```

---

## 🚨 Common Pitfalls & Solutions

### Problem 1: Poor Retrieval Quality
**Symptoms**: Irrelevant documents retrieved
**Solutions**:
```python
# Better chunking strategy
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Smaller chunks
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Better metadata
for doc in documents:
    doc.metadata.update({
        "section": extract_section(doc),
        "document_type": classify_document_type(doc),
        "keywords": extract_keywords(doc)
    })

# Hybrid retrieval
ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.6, 0.4]
)
```

### Problem 2: Slow Query Performance
**Solutions**:
- Use async operations
- Implement caching
- Pre-compute embeddings
- Use approximate search

### Problem 3: Context Window Limitations
**Solutions**:
- Implement document re-ranking
- Use map-reduce for long documents
- Summarize retrieved chunks before LLM

---

## 📚 Next Steps

### Beginner → Intermediate
1. Add metadata filtering
2. Implement hybrid retrieval
3. Add document updates
4. Basic evaluation metrics

### Intermediate → Advanced
1. Knowledge graph integration
2. Multi-modal RAG (text + images)
3. Real-time document streaming
4. Advanced evaluation frameworks

### Advanced → Production
1. Distributed vector stores
2. Advanced caching strategies
3. Monitoring and alerting
4. A/B testing framework

---

## 🔗 Related Guides

- [Getting Started](./getting-started.md) - Foundation concepts
- [Conversational AI](./conversational-ai.md) - Combine with chatbots
- [AI Agents](./ai-agents.md) - RAG-powered agents
- [Deployment](./deployment.md) - Production scaling

---

*Last updated: {{ date }}*  
*Difficulty: 🟡 Intermediate*  
*Estimated time: 6-12 hours*
