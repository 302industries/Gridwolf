"""Regression tests for ICS timestamp compatibility."""

from datetime import datetime, timezone

from app.models.ics import PcapFile, Session, utcnow


def test_ics_utcnow_returns_naive_utc():
    """UTC timestamps must match PostgreSQL's naive columns."""
    before = datetime.now(timezone.utc).replace(tzinfo=None)

    result = utcnow()

    after = datetime.now(timezone.utc).replace(tzinfo=None)

    assert result.tzinfo is None
    assert before <= result <= after


def test_ics_timestamp_columns_are_naive():
    """Model definitions must agree with the UTC helper."""
    for model in (Session, PcapFile):
        column = model.__table__.c.created_at
        assert column.type.timezone is False
