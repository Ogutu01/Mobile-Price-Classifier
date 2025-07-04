
# Mobile Price Range Classifier
![Phone Image](data/images/phone1_image.jpg)

## Description

Predicts the price range of mobile phones based on hardware specifications using machine learning.

This project takes input features like RAM, battery life, camera specs, screen, and connectivity attributes to build models that classify mobiles into one of four price categories:
- **0** – low cost  
- **1** – medium cost  
- **2** – high cost  
- **3** – very high cost

---

## 🚀 Features

- ✅ Supports multiple ML algorithms: Logistic Regression, KNN, SVM, Decision Trees, Random Forest  
- ✅ Includes EDA, preprocessing, and feature engineering  
- ✅ Generates model evaluation reports: accuracy, confusion matrix, classification report  
- ✅ Saves the best-performing model for reuse/prediction  

---

## 🧰 Technologies Used

- Python 3.x  
- pandas, NumPy  
- scikit-learn  
- Jupyter Notebook  
- matplotlib / seaborn  

---

## 📦 Installation

### Prerequisites

- Python 3.8+  
- Git  
- pip  

### Steps

```bash
git clone https://github.com/Ogutu01/Mobile-Price-Classifier.git
cd Mobile-Price-Classifier

# (Optional) create & activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
````

If `requirements.txt` is missing, manually install:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

---

## 🧪 Usage

### 1. Run the Jupyter notebook

```bash
jupyter notebook
```

Open `notebooks/Mobile_Price_Classifier.ipynb` to explore EDA, preprocessing steps, model training, and evaluation.

### 2. Train & evaluate models

Inside the notebook:

* Preprocess dataset (handle missing values, scale features)
* Split into train/test
* Train multiple classifiers
* Evaluate using metrics & select the best model
* Save the winning model as `model.pkl`

### 3. Load model & predict

```python
from src.predict import load_model, predict_price

model = load_model("model.pkl")

features = {
  "battery_power": 1500,
  "ram": 2048,
  "pc": 12,
  "fc": 5,
  # Add all required features...
}

print("Predicted price range:", predict_price(model, features))
```

---

## 📂 Project Structure

```
Mobile-Price-Classifier/
├── data/
│   └── images
    └──test_data_with_oredictions.csv
    └──test.csv
    └──train.csv
├── notebooks/
│   └── index.ipynb
├── model.pkl
├── requirements.txt
└── GEN_AI(Updated)_README.md
```

## 🛠️ Troubleshooting

* **Jupyter won't run**: Ensure `jupyter` is installed and you're in the project root.
* **Module import errors**: Activate your virtual environment before running scripts/notebooks.
* **Error loading model**: Make sure `model.pkl` exists and paths in `app.py` are correct.
* **Poor model accuracy**: Tune hyperparameters, try different test/train splits, or add more features.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make changes and add tests
4. Commit with clear messages (`git commit -m "Add XYZ"`)
5. Push to your branch and open a PR

Please follow existing code style and document new features.

---

## 📄 License

This project is open-source and distributed under the **MIT License**. See the [LICENSE](./LICENSE) file for more details.

---

## 🙋 Support & Contact

Got questions or found a bug? Please open an [issue](https://github.com/Ogutu01/Mobile-Price-Classifier/issues) or contact via email.
```