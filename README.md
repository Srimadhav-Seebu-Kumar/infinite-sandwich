# 🥪 Infinite Sandwich Generator

Absurdist, generative project that builds nonsense sandwiches from real and fictional ingredients, scored by models trained on random data. Streamlit UI, image gen, style LMs.

## Features

- 🎲 **Random Sandwich Generation**: Creates unique combinations from fictional ingredients
- 📊 **AI Scoring System**: Mock ML models rate sandwiches on absurdity, creativity, and edibility  
- 🎨 **Interactive UI**: Built with Streamlit for easy interaction
- 📜 **Sandwich History**: Track your generated sandwich creations
- ⚡ **CI/CD Pipeline**: Automated testing and deployment

## Installation

```bash
# Clone the repository
git clone https://github.com/Srimadhav-Seebu-Kumar/infinite-sandwich.git
cd infinite-sandwich

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run src/app.py
```

## Example Output

### ✨ The Bewildering Mystery

**🥗 Ingredients:**
• quantum mustard
• interdimensional cheese  
• temporal lettuce
• binary bologna
• encrypted eggplant

**🎭 Flavor Profile:** Bewildering

**📊 AI Scores:**
- **Absurdity:** 8.7/10
- **Creativity:** 9.2/10  
- **Edibility:** 1.4/10 ⚠️ (Lower is more realistic)
- **Total Score:** 6.4/10

*Generated at: 2025-09-22 00:48:15*

---

### 🎯 Project Structure

```
infinite-sandwich/
├── src/
│   └── app.py              # Main Streamlit application
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── LICENSE               # MIT License
└── README.md            # This file
```

## Development

### Running Tests
```bash
pytest -v
```

### Code Formatting
```bash
black .
flake8 .
```

### Local Development
```bash
streamlit run src/app.py --server.port 8501
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`) 
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

🤖 *Powered by completely fictional AI models and random number generators. No actual sandwiches were harmed in the making of this application.*
