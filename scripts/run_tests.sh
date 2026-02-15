#!/bin/bash

# 1️⃣ Activate virtual environment
echo "Activating virtual environment..."
# Windows
source ../virtualenv/Scripts/activate
# macOS/Linux (uncomment if on Mac/Linux)
# source ../virtualenv/bin/activate

# 2️⃣ Navigate to your Dash project
cd ../my_dash_project

# 3️⃣ Run your test file
echo "Running automated tests from test_app.py..."
python test_app.py

# 4️⃣ Done
echo "All tests finished!"
