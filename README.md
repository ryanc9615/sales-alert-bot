
## Setup

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/sales-alert-bot.git
   cd sales-alert-bot
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the project root with the following variables:
     ```
     SMTP_SERVER=smtp.gmail.com
     SMTP_PORT=587
     SMTP_USERNAME=your_email@gmail.com
     SMTP_PASSWORD=your_app_password
     EMAIL_FROM=your_email@gmail.com
     EMAIL_TO=recipient@example.com
     ```
   - For Gmail, you must use an [App Password](https://myaccount.google.com/apppasswords) instead of your regular password.

## Usage

### Running the Bot

1. **Ensure your sales data is in the `data/sales/` directory** as CSV files named by date (e.g., `2025-04-27.csv`).

2. **Run the script:**
   ```sh
   python src/main.py
   ```

3. **Check your email** for the sales alert report.

### Scheduling

To run the bot daily, you can use:
- **Cron (Linux/Mac):**
  ```sh
  0 8 * * * cd /path/to/sales-alert-bot && /path/to/venv/bin/python src/main.py
  ```
- **Task Scheduler (Windows):**
  - Create a task to run `src/main.py` daily.

## Customization

- **Sales Data:** Modify `sales_analyser.py` to adjust the analysis logic or data source.
- **Email Format:** Update `emailer.py` to change the email subject, body, or recipient.

## Troubleshooting

- **Email Not Sending:** Check your SMTP settings and ensure your App Password is correct.
- **No Data Found:** Verify that your CSV files are in the correct directory and named correctly.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue or contact [your-email@example.com](mailto:your-email@example.com).