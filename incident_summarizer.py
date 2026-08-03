error_count = 0
Warning_count = 0
information_count = 0

with open("app.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        else:
            information_count += 1
with open("summary_report.txt", "w") as report_file:
    report_file.write(f"Total Errors: {error_count}\n")
    report_file.write(f"Total Warnings: {Warning_count}\n")
    report_file.write(f"Total Information Messages: {information_count}\n")
    print("Summary report generated: summary_report.txt")