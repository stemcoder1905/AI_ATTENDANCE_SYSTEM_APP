# SnapClass — AI Attendance App

Streamlit-based desktop/web app to simplify classroom attendance using face and voice recognition.

## Summary

`SnapClass` provides an interface for teachers and students to take and manage attendance using two biometric pipelines: face recognition and voice-based verification. The app includes teacher dashboards, student screens, subject management, and an auto-enroll flow via a join code.

## Key Features

- Teacher dashboard for creating subjects and viewing attendance
- Student screen for joining classes and marking attendance
- Face recognition pipeline for camera-based attendance
- Voice recognition pipeline for audio-based attendance
- Auto-enroll via `join-code` query parameter
- Supabase-backed database for storing users, subjects and attendance

## Tech Stack

- Python 3.8+
- Streamlit (UI)
- NumPy, pandas
- dlib / face_recognition (face pipeline)
- librosa, resemblyzer (voice pipeline)
- Supabase (database)

Dependencies are listed in `requirements.txt`.

## Project Structure

- `app.py` — Streamlit entrypoint
- `src/screens/` — screen modules (`home_screen`, `teacher_screen`, `student_screen`)
- `src/components/` — UI dialogs and components
- `src/pipelines/` — `face_pipeline.py` and `voice_pipeline.py`
- `src/database/` — `config.py`, `db.py` (Supabase client and helpers)
- `src/ui/` — base layout components

## Configuration

1. Add Supabase credentials to Streamlit secrets (or set them in `st.secrets`):

```
[SUPABASE]
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```

The app reads `st.secrets["SUPABASE_URL"]` and `st.secrets["SUPABASE_KEY"]` in `src/database/config.py`.

Note: some dependencies (e.g. `dlib`, `face_recognition`) require native build tools (CMake, a C++ compiler) on your platform.

## Installation (local)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\\Scripts\\activate      # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Usage notes

- To auto-enroll a student using a join code, open the app with a query parameter: `?join-code=<CODE>` and the app will switch to the student flow.
- Ensure a working camera/microphone when using face or voice pipelines.

## Contributing

Contributions and bug reports are welcome. Please open issues describing steps to reproduce and expected behavior.

## License

This project does not include a license file. Add one if you plan to open source the code.
# ai-attendance-project-app