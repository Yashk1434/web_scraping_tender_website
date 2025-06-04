# 📑 CPWD eTender Data Scraper

A Python-based web scraping project that automates the extraction of tender information from the [CPWD eTender website](https://etender.cpwd.gov.in/) and saves it into a clean CSV file.

---

## 📖 Project Overview

This project uses **Selenium** to navigate through the CPWD eTender portal, handle a JavaScript alert popup, interact with dropdowns, and extract details of the first 20 tenders listed under the **New Tenders → All** tab. The extracted tender data is then stored in a CSV file with well-defined column names.

---

## 🖥️ Project Demo

**📌 Tender Data converted to CSV**

![Tender Data to CSV](https://github.com/user-attachments/assets/4f3733bd-ac1a-488a-96f7-447b3615339c)

**📌 Tenders Page Scraping**

![Website Tenders Page](https://github.com/user-attachments/assets/a2a9ed64-ae0a-4c00-b59c-596fdd383b85)

---

## 📌 Features

- Automated scraping of first **20 tenders**
- Handles **JavaScript alert popup** on site load
- Interacts with **dropdown to select number of tenders displayed**
- Waits for data to load before scraping
- Saves data into a **CSV file** with clean, renamed headers

---

## 📦 Tech Stack

- **Python**
- **Selenium**
- **Pandas**

---

## 📑 CSV Output Columns

| Original Field                        | Renamed Column         |
|:-------------------------------------|:----------------------|
| NIT/RFP NO                           | `ref_no`               |
| Name of Work / Subwork / Packages    | `title`                |
| Estimated Cost                       | `tender_value`         |
| Bid Submission Closing Date & Time  | `bid_submission_end_date` |
| EMD Amount                           | `emd`                  |
| Bid Opening Date & Time              | `bid_open_date`        |

---

## 📂 How to Run

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the scraper:
    ```bash
    python run.py
    ```

3. Check the generated `tender_data.csv` file in your project directory.

---

## 📖 About Me

I’m a passionate Python developer specializing in **computer vision, AI/ML, IoT systems**, and **web-based applications**. I enjoy integrating real-time workflows using tools like **Flask**, **OpenCV**, and **Hugging Face Transformers**. This project strengthened my skills in web automation, data handling, and dynamic web interaction.

---
