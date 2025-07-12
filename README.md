# 🏅 Olympic Data Analysis Web App

**A Streamlit application for exploring, visualizing, and analyzing 120 years of Olympic data** sourced from [Kaggle](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results).

## 🚀 Features

- **Medal Tally**: View country rankings by gold, silver, bronze, and total medals.
- **Overall Trends**:
  - Editions, hosts, sports, events, athletes, and countries over time.
  - Heatmap of events per sport across years.
- **Country Insights**:
  - Medals by year for a selected country.
  - Top-performing athletes per country.
- **Athlete Analysis**:
  - Athlete age distribution by medal type and sport.
  - Height vs. weight scatter plots with medal and gender filters.
  - Historical comparison of male vs. female participation.

![Capture12](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/6a02f414-3163-4697-841b-0230323947bc)
![Capture11](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/913fcd04-4746-45f2-8054-ea626a88efca)
![Capture10](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/1add5552-e632-4ff2-b220-b2d1eb418185)
![Capture8](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/05fd76ca-951d-4cd3-a612-934b751abe72)
![Capture7](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/da121e04-b7e8-471c-b4d0-b76658c9ebef)
![Capture5](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/bcdbdfad-b292-4c24-8dc1-2c7906bde12c)
![Capture4](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/9427f6e1-2c3e-4721-b03e-f73d030cce56)
![Capture3](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/8f35b816-5a36-4234-9bb2-8327280e668a)
![Capture2](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/12421a77-e0f8-448f-bdd8-cf841e82e69c)
![Capture](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/45fd30b2-040d-431d-ae36-657a104ce149)
![Capture 13](https://github.com/minhazriyam/olympic_data_analysis_web_app/assets/107611294/dea4fe46-e166-4f20-8bbc-cfb8e05c80f8)

## 🛠️ Tech Stack

- **Streamlit** – for the interactive web interface.
- **Python** – core development.
- **Pandas, NumPy** – data processing.
- **Matplotlib, Seaborn, Plotly** – visualizations.
- **Heroku** – deployment platform.

---

## 📦 Repository Contents

```
├── app.py            # Main Streamlit app
├── helper.py         # Plotting & logic functions
├── preprocessor.py   # Data loading & cleaning routines
├── requirements.txt  # Python dependencies
├── setup.sh          # Environment setup script
└── Procfile          # Heroku startup config
```

---

## ⚙️ Installation & Local Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/minhazriyam/olympic_data_analysis_web_app.git
   cd olympic_data_analysis_web_app
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**  
   - Download `athlete_events.csv` from Kaggle.
   - Place it inside the project directory or modify `preprocessor.py` to point to your file path.

4. **Launch the app**  
   ```bash
   streamlit run app.py
   ```

5. **Visit**  
   Open your browser at `http://localhost:8501`.

---

## 🎯 Usage Guide

- **Home / Medal Tally**: Compare countries’ medal counts by selecting a year range.
- **Overall Analysis**: Explore Olympic history trends and statistics with interactive graphs.
- **Country-wise**: Select a nation to get detailed medal breakdowns and top athletes.
- **Athlete-wise**: Analyze athlete demographics, physical stats, and participation over time.

---

## 👨‍💻 Who Is It For?

- Sports analysts and historians seeking historical Olympic insights.
- Data science enthusiasts learning Streamlit and EDA techniques.
- Coaches/athletes looking to benchmark performance trends.

---

## 🔁 Future Improvements

- **Geospatial maps** of medal distribution by country.
- **Machine learning** models to predict future medal counts.
- **Correlation analysis** between athlete attributes like age, height, weight, sport, and medal success.
- **Multi-language support** and enhanced UI/UX.

---

## 🧩 How to Contribute

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-yourfeature`)  
3. Commit your changes (`git commit -m "Add awesome feature"`)  
4. Push (`git push origin feature-yourfeature`)  
5. Open a Pull Request—let’s collaborate!

---

## 📄 License & Contact

This project is available under the **MIT License**.
