from datetime import datetime


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        try:
            config._metadata.clear()
        except Exception:
            pass


def pytest_html_report_title(report):
    report.title = "RezwanAuto Test Report"


def pytest_html_results_summary(prefix, summary, postfix, session):
    prefix.clear()
    prefix.append(
        "<p>This report summarizes the RezwanAuto Selenium test run in a clean, visual format. "
        "Use the filters to focus on failed or skipped cases.</p>"
    )
    prefix.append(
        f"<p>Total tests collected: {session.testscollected}. "
        f"Run started at {datetime.now():%Y-%m-%d %H:%M:%S}.</p>"
    )
    summary.clear()
    summary.append(
        "<p>The test table below is color-coded by outcome. Expand a row for details and attach logs or screenshots.</p>"
    )
