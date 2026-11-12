import sys
import duckdb
import subprocess

# Python version
assert sys.version_info.major == 3, "Python version must be 3.13"
assert sys.version_info.minor == 13, "Python version must be 3.13"

# DuckDB check
con = duckdb.connect()
assert con.execute("SELECT 21 AS answer").fetchone()[0] == 21, "DuckDB failure!"

# dbt check
result = subprocess.run(['dbt', '--version'], capture_output=True, text=True)

assert result.returncode == 0 and "duckdb" in result.stdout, "dbt failure!"

# If all lines above pass, below should run
print("ENVIRONMENT OK")