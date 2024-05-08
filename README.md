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
    
2. **Set Up a Python Virtual Environment**:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Python dependencies**:
pip install -r requirements.txt


4. **Run the FastAPI server**:
uvicorn main:app --reload

This command starts the FastAPI server with live reloading.

### Setting Up the Frontend (bash, MacOS)

1. **Navigate to the frontend directory**:
cd ../frontend


2. **Install Node dependencies**:
npm install


3. **Start the React development server**:
npm start

The server typically runs at `http://localhost:3000`.

## Usage

1. **Web Interface**: Access the interface at `http://localhost:3000`.
2. **Input YouTube Video URL**: Enter the URL of the lecture video to process.
3. **Generate Flashcards**: The backend extracts text, identifies key concepts, and presents them as flashcards on the frontend.

## Backend Detailed Workflow

- **YouTube Document Retrieval**: The `YoutubeProcessor` uses `YoutubeLoader` to fetch video scripts, which are then split into manageable documents.
- **Concept Extraction**: `GeminiProcessor` employs Google Vertex AI and Gemini models to extract key concepts, showcasing the application of generative AI in educational technology.
- **Error Handling and Logging**: Extensive logging to trace steps and handle errors gracefully.

##Acknowledgement
This project, "Gemini Dynamo," was developed with the invaluable guidance and structured mission tasks provided by Radical AI. I extend my heartfelt thanks to Rex, the AI coach, whose expert advice steered me through the complexities of the project. Additionally, I am grateful for the instructional videos created by the Radical AI team. These resources not only explained the nuances of the code but also provided detailed insights into the subtleties of the project, enhancing my understanding and execution of the tasks. Their support has been instrumental in the successful completion of this project.

