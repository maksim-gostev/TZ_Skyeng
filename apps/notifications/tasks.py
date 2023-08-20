from celery import shared_task
from reports.services import ReportReviewService
from reports.models import Report, Status


@shared_task
def review_reports():
    reports = Report.objects.filter(status=Status.pending).all()

    for report in reports:
        report_instance = ReportReviewService(report)
        report_instance.save_results()
        report_instance.send_email_results()

    return f'{len(reports)} reports were reviewed.'
