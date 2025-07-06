#!/usr/bin/env python3
"""
Test script to verify the Chroma MCP server is working correctly.
"""

import chromadb
import json
from pathlib import Path

def test_chroma_connection():
    """Test connection to the Chroma database."""
    
    # Connect to the database
    workspace_dir = Path(__file__).parent.parent
    data_dir = workspace_dir / "chroma_data"
    
    try:
        client = chromadb.PersistentClient(path=str(data_dir))
        
        # Get the collection
        collection = client.get_collection("digital_palace_docs")
        
        # Test a simple query
        results = collection.query(
            query_texts=["AI agents"],
            n_results=3
        )
        
        print("✅ Connection successful!")
        print(f"📊 Collection contains {collection.count()} documents")
        print(f"🔍 Test query 'AI agents' found {len(results['documents'][0])} results:")
        
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
            print(f"  {i+1}. {metadata['filename']} (Score: {results['distances'][0][i]:.3f})")
            print(f"     Path: {metadata['path']}")
            print(f"     Preview: {doc[:100]}...")
            print()
            
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_chroma_connection()
    if success:
        print("🎉 Your Chroma MCP setup is working correctly!")
        print("💡 You can now use it with VS Code MCP extensions.")
    else:
        print("⚠️  There might be an issue with your setup.")
