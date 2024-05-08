# Youtube Video Flashcard Generator

## Overview
Welcome to the Video Transcript Flashcard Wizard! This application is a boon for educators, utilizing cutting-edge technology to generate flashcards from YouTube video transcripts. Behind the scenes, it leverages FastAPI for the backend, while employing Google's Vertex AI and Gemini models for video content processing. The frontend is crafted with React, offering an intuitive and interactive user experience. Dive into the realm of advanced generative AI techniques, extracting scripts, summarizing text, and pinpointing key educational concepts effortlessly.

## Key Features
- **Effortless Script Extraction**: Powered by Langchain modules, ensuring precise extraction of text from YouTube videos.
- **AI-driven Concept Extraction**: Harnessing the prowess of Google's Gemini and Vertex AI API to identify pivotal educational concepts.
- **Secure API Integration**: Safeguarding data privacy and security with seamless integration and properly configured Google service accounts.
- **Engaging Flashcard Generation**: Transforming identified concepts into dynamic flashcards, fostering effective and enjoyable learning experiences.

## Project Structure
```bash
project-root/
│
├── backend/             # FastAPI application
│   ├── main.py          # Entry point for the FastAPI server
│   ├── genai.py         # Core processing scripts for video analysis
│   └── requirements.txt # Python dependencies
│
├── frontend/            # React application
    ├── src/             # Source files for the frontend
    ├── public/
    ├── package.json     # NPM dependencies and scripts
    ├── README.md        # Frontend documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup (bash, MacOS)

1. **Navigate to the backend directory**:
```bash
cd backend
```    
2. **Set Up a Python Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

5. **Run the FastAPI server**:
```bash
uvicorn main:app --reload
```

This command starts the FastAPI server with live reloading.

### Setting Up the Frontend (bash, MacOS)

1. **Navigate to the frontend directory**:
```bash
cd ../frontend
```

3. **Install Node dependencies**:
```bash
npm install
```

4. **Start the React development server**:
```bash
npm start
```

## Usage

1. **Web Interface**: Access the interface at localhost
2. **Input YouTube Video URL**: Enter the URL of the lecture video to process.
3. **Generate Flashcards**: The backend extracts text, identifies key concepts, and presents them as flashcards on the frontend.

## Backend Detailed Workflow

- **YouTube Document Retrieval**: The `YoutubeProcessor` uses `YoutubeLoader` to fetch video scripts, which are then split into manageable documents.
- **Concept Extraction**: `GeminiProcessor` employs Google Vertex AI and Gemini models to extract key concepts, showcasing the application of generative AI in educational technology.
- **Error Handling and Logging**: Extensive logging to trace steps and handle errors gracefully.

