from sales_analyser import analyse_sales
from emailer import send_email

def main():
    print("Starting sales analysis...")

    # Generate the report
    report = analyse_sales()
    print(f"Report generated: {report}")

    # Send the email
    print("Sending email...")
    send_email("Sales Alert Report", report)
    print("Email sent successfully!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

