"""
Health tests for MicroSaaS Exit Kit.
Signature: Mourad.Soltani
"""

import subprocess
import sys
from pathlib import Path

def test_health_flag():
    """Health check must pass."""
    result = subprocess.run(
        [sys.executable, "exitkit.py", "--health"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    assert "Health check: OK" in result.stdout
    assert "Mourad.Soltani" in result.stdout

def test_generate_files(tmp_path):
    """Generation must produce expected files with signature."""
    result = subprocess.run(
        [
            sys.executable, "exitkit.py",
            "--product", "TestKit",
            "--niche", "testing",
            "--mrr", "100",
            "--output-dir", str(tmp_path)
        ],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    buyer = tmp_path / "BUYER_NOTES.md"
    outreach = tmp_path / "OUTREACH_TEMPLATES.md"
    assert buyer.exists()
    assert outreach.exists()
    content = buyer.read_text()
    assert "Mourad.Soltani" in content
    assert "TestKit" in content

if __name__ == "__main__":
    # Simple runner for health
    test_health_flag()
    print("All health tests passed.")
