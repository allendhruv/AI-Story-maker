🧠 Product Specification Extractor using Azure AI Vision
->This project extracts key product specifications such as dimensions, weight, volume, voltage, and wattage directly from product images using Azure AI Vision OCR and intelligent text analysis.

🔍 Key Features
->Leverages Azure's Computer Vision API for robust OCR

->Extracts product specs in formats like:

->"12 cm", "2.5 kg", "220 volt", etc.

->Designed for large-scale image datasets (e.g., e-commerce product listings)

O->utputs clean CSV files for indexing or model training

🔧 Tech Stack
->Python

->Azure Cognitive Services (Vision API)

->Regular Expressions for pattern matching

->Modular architecture (image_analysis.py, sns.py, pk_openai.py, etc.)

🛠️ How to Run This Azure AI Product Extractor Locally
🔗 Step-by-Step Tutorial
1. Clone the Repository
git clone https://github.com/yourusername/product-spec-extractor.git
cd product-spec-extractor

2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows

3.  Install Required Python Modules
pip install -r requirements.txt

4. Set Up Azure AI Credentials
You need an Azure Computer Vision API key and endpoint.

Create a free Azure account: https://azure.microsoft.com/free

Go to the Azure Portal → Create a Computer Vision resource

Copy your Key and Endpoint

5. Add Your Azure Credentials
Edit or create a file (e.g., .env or directly in your code like pk_openai.py) and add:
AZURE_API_KEY = "your_azure_api_key"
AZURE_ENDPOINT = "your_azure_endpoint"

6. Run the Code
python imageink.py
