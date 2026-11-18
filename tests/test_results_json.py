"""The dashboard's results.json carries fill.py's numbers unchanged, and adding it changed no deliverable."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import fill  # noqa: E402

INPUTS = ROOT / "examples" / "acme-inputs.json"


@pytest.fixture(scope="module")
def res(tmp_path_factory):
    out = tmp_path_factory.mktemp("json") / "results.json"
    subprocess.run([sys.executable, str(ROOT / "fill.py"), "math", str(INPUTS), "--json", str(out)], check=True, capture_output=True)
    return json.loads(out.read_text())


def test_plan_matches_compute(res):
    m = fill.compute(fill.resolve(json.loads(INPUTS.read_text())))
    for k, v in m.items():
        if k != "monthly":
            assert res["plan"][k] == pytest.approx(v)
    funnel = {f["key"]: f for f in res["funnel"]}
    for k in ("pipeline_goal", "saos", "sqls", "mqls", "capture_budget", "creation_budget", "budget"):
        assert funnel[k]["total"] == pytest.approx(m[k])
        assert funnel[k]["per_month"] == pytest.approx(m["monthly"][k])


def test_budget_adds_up(res):
    chans = res["budget"]["channels"]
    assert sum(c["total"] for c in chans) == pytest.approx(res["plan"]["budget"])
    assert len(res["budget"]["months"]) == res["months"]
    assert sum(r["spend"] for r in res["budget"]["months"]) == pytest.approx(res["plan"]["budget"])
    assert res["budget"]["months"][0]["month"] == "Jan 2027"


def test_inputs_mark_defaults(res):
    by = {i["key"]: i for i in res["inputs"]}
    assert by["deal_size"]["default"] is False and by["win_rate"]["default"] is True
    assert by["start_date"]["value"] == "2027-01-04"


def test_tasks_match_task_csv(res):
    rows = (ROOT / "deliverables" / "recurring-tasks.csv").read_text().strip().splitlines()
    assert len(res["tasks"]) == len(rows) - 1
    assert res["tasks"][0]["first_due"] == "2027-01-04"


def test_plan_deliverables_unchanged(tmp_path):
    subprocess.run([sys.executable, str(ROOT / "fill.py"), "plan", str(INPUTS), "--out", str(tmp_path)], check=True, capture_output=True)
    for name in ("planning-doc.md", "budget-tracker.csv", "recurring-tasks.csv", "regular-updates.md", "experiment-database.csv"):
        assert (tmp_path / name).read_text() == (ROOT / "examples" / "acme" / name).read_text(), name
