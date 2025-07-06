#!/usr/bin/env python3
"""
Initialize Chroma database with markdown files from the Digital Palace repository.
This script will index all markdown files to make them searchable via the MCP server.
"""

import os
import sys
import chromadb
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_chroma_db():
    """Initialize Chroma database with markdown files."""
    
    # Get the workspace directory
    workspace_dir = Path(__file__).parent.parent
    data_dir = workspace_dir / "chroma_data"
    
    # Create data directory if it doesn't exist
    data_dir.mkdir(exist_ok=True)
    
    # Initialize Chroma client
    client = chromadb.PersistentClient(path=str(data_dir))
    
    # Create or get collection
    collection_name = "digital_palace_docs"
    try:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "Digital Palace markdown documents"}
        )
        logger.info(f"Created new collection: {collection_name}")
    except Exception as e:
        # Collection might already exist
        collection = client.get_collection(name=collection_name)
        logger.info(f"Using existing collection: {collection_name}")
    
    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk(workspace_dir):
        # Skip hidden directories and common excludes
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'tmp', 'venv', '__pycache__']]
        
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                md_files.append(file_path)
    
    logger.info(f"Found {len(md_files)} markdown files")
    
    # Process files in batches
    batch_size = 100
    for i in range(0, len(md_files), batch_size):
        batch = md_files[i:i + batch_size]
        
        documents = []
        metadatas = []
        ids = []
        
        for file_path in batch:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Create relative path for ID
                rel_path = file_path.relative_to(workspace_dir)
                file_id = str(rel_path).replace('/', '_').replace('.md', '')
                
                documents.append(content)
                metadatas.append({
                    "filename": file_path.name,
                    "path": str(rel_path),
                    "directory": str(file_path.parent.relative_to(workspace_dir)),
                    "size": len(content)
                })
                ids.append(file_id)
                
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                continue
        
        # Add to collection
        if documents:
            try:
                collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
                logger.info(f"Added batch {i//batch_size + 1}: {len(documents)} documents")
            except Exception as e:
                logger.error(f"Error adding batch to collection: {e}")
    
    # Get collection stats
    count = collection.count()
    logger.info(f"Collection '{collection_name}' now contains {count} documents")
    
    return collection

if __name__ == "__main__":
    try:
        collection = initialize_chroma_db()
        print(f"✅ Successfully initialized Chroma database with {collection.count()} documents")
        print(f"🔍 Your documents are now searchable via the MCP server!")
        print(f"💡 Use the 'Start Chroma MCP Server' task in VS Code to begin using it.")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        sys.exit(1)
