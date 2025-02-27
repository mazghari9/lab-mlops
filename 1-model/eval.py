import pandas as pd
from evidently.report import Report
from evidently.metric_preset import ClassificationPreset, DataDriftPreset

FEATURE_NAMES = [
    "lead_time", "arrival_date_week_number", "arrival_date_day_of_month", 
    "stays_in_weekend_nights", "stays_in_week_nights", "adr", 
    "adults", "children", "babies", "meal", "market_segment", 
    "distribution_channel", "is_repeated_guest", "previous_cancellations", 
    "previous_bookings_not_canceled", "reserved_room_type", "assigned_room_type", 
    "booking_changes", "deposit_type", "agent", "company", "days_in_waiting_list", 
    "customer_type", "required_car_parking_spaces", "total_of_special_requests", 
    "reservation_status", "reservation_status_date", "room_type"
]  

reference_data = pd.DataFrame([
    [120, 5, 10, 1, 2, 110.0, 2, 0, 0, 2, 3, 0, 1, 0, 1, 3, 0, 1, 0, 1, 2, 0, 1, 0, 2, 1, 3, 0, 0, 0], 
    [80, 12, 15, 0, 3, 90.5, 2, 0, 0, 1, 2, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 2, 0, 1, 1, 2, 5, 1, 1, 1],
    [50, 8, 12, 1, 1, 80.0, 2, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 3, 1, 0, 1],
], columns=FEATURE_NAMES + ["target", "prediction"])

current_data = pd.DataFrame([
    [100, 3, 7, 1, 1, 95.0, 2, 0, 0, 3, 3, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 7, 1, 0, 0], 
    [150, 10, 20, 2, 0, 125.0, 1, 1, 0, 2, 4, 0, 1, 0, 1, 3, 0, 1, 0, 1, 2, 0, 1, 0, 3, 1, 4, 0, 1, 1],
    [60, 8, 12, 1, 1, 70.0, 2, 0, 1, 2, 3, 0, 0, 0, 1, 3, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 5, 0, 0, 1],
], columns=FEATURE_NAMES + ["target", "prediction"])

classification_report = Report(metrics=[ClassificationPreset()])
classification_report.run(reference_data=reference_data, current_data=current_data)
classification_report.save_html("reports/hotel_booking_performance.html")

drift_report = Report(metrics=[DataDriftPreset()])
drift_report.run(reference_data=reference_data, current_data=current_data)
drift_report.save_html("reports/hotel_booking_drift.html")

print("✅ Model monitoring reports generated!")
