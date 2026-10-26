@echo off
REM GEO Optimizer - one-click local launcher
REM Repo: https://github.com/Auriti-Labs/geo-optimizer-skill (v4.17.1, MIT)
REM Main UI + API: http://127.0.0.1:8000  (FastAPI serves the demo homepage)
REM Astro frontend: http://127.0.0.1:4321 (dev preview; its /api proxy is
REM   not applied by Astro 6 dev server - use :8000 for full functionality)

cd /d "%~dp0"

echo [1/2] Starting FastAPI backend on http://127.0.0.1:8000 ...
start "GEO-Backend" cmd /k ".venv\Scripts\geo-web.exe --host 127.0.0.1 --port 8000"

echo [2/2] Starting Astro frontend on http://127.0.0.1:4321 ...
cd frontend
start "GEO-Frontend" cmd /k "npm run dev -- --host 127.0.0.1 --port 4321"
cd ..

echo.
echo ============================================
echo  Main UI + Audit API : http://127.0.0.1:8000
echo    - Homepage with audit form: /
echo    - Health check: /health
echo    - Audit API:    /api/audit?url=^<site^>
echo  Astro dev preview   : http://127.0.0.1:4321
echo  CLI                 : .venv\Scripts\geo audit --url https://yoursite.com
echo ============================================
echo Close the two popped-up windows to stop both services.
