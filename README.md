# DayFlow RPC

**A time-aware Discord Rich Presence that mirrors my daily routine**

> My first real-world Python project after completing **MIT 6.100L (Introduction to Computer Science and Programming)**.

---

## Why this project exists

This project started from a **real-life problem**, not a technical one.

I follow a strict daily routine (study blocks, guitar practice, gym, rest), and I often stay in deep focus for long periods.  
Because of this, people close to me — especially my girlfriend — would sometimes feel unsure or worried when I was unavailable.

Not because of a lack of care, but because:
- she didn’t always know *what I was doing*
- or *how long I would be busy*
- or *when I would be free again*

Explaining this manually every day was inconsistent and tiring for both of us.

So I asked myself:

> *Can I make my routine visible automatically, without interrupting my work or constantly explaining myself?*

Since we already communicate on Discord, I decided to use **Discord Rich Presence** as a passive, always-available signal of:
- what I’m currently doing
- how long this state will last
- what comes next

That question became **DayFlow RPC**.

---

## What DayFlow RPC does

- Runs **locally** on my machine
- Tracks the **current time of day**
- Maps time → **activity mode** (study, guitar, gym, rest, sleep)
- Updates **Discord Rich Presence** safely using the official RPC mechanism
- Shows a **countdown** to when the current state ends
- Indicates what activity comes **next**
- Handles **midnight rollover** correctly
- Avoids unnecessary updates to prevent external system spam

This allows someone viewing my status to understand my availability **without needing to ask**.

This is **not a Discord bot** and does **not** automate messages or accounts.

---

## Key ideas used

While building this as a beginner project, I encountered real system-design concepts:

- **Finite State Machine**  
  (time → current mode)
- **Time quantization**  
  (continuous representation of hours and minutes)
- **External system constraints**  
  (safe update frequency)
- **Human-centric design**  
  (accuracy matters because a real person is reading it)
- **Day rollover handling**  
  (23 → 0 transition)

---

## How it works (high level)

Current Time
↓
Mode Selector (state machine)
↓
Time Remaining Calculation
↓
Discord Rich Presence Update

The program runs continuously and updates only when it is safe and meaningful.

---

## Example modes

- Deep Focus 🚀 (study)
- Guitar Practice 🎸
- Mission Mode: Growth 🧠
- Chill Time 🍿
- Gym 🏋️‍♂️
- Unwind & Reset 🌙
- Sleep 💤

Each mode includes:
- a clear label
- a description
- an end time
- a countdown to the next state

---

## Tech stack

- Python 3
- `pypresence` (Discord Rich Presence)
- Standard library only (`datetime`, `time`, `math`)

No frameworks. No databases. No web servers.

---

## What I learned from this project

- Real systems are more about **state and timing** than syntax
- External systems don’t always reflect updates instantly
- Designing for **human reassurance** changes technical decisions
- Handling time correctly is harder than it looks
- Small, useful tools teach more than large demo projects

---

## Limitations (by design)

- Schedule is currently hardcoded
- Single-user, personal-use tool
- No configuration files or UI
- No persistence between restarts

These choices were intentional to keep the focus on learning core logic.

---

## How to run

1. Install Python 3
2. Install dependency:
   ```bash
   pip install pypresence
   ```
3. Open the Discord desktop app
4. Run the script:
    ```
     python dayflow_rpc.py
    ```

Here’s a **clean, copy-paste-ready README section** you can drop straight into your repo.
It’s written so **any Linux user** can automate it without confusion.

---

## 🚀 Run Automatically on Login (Linux / GNOME)

This project can run **automatically in the background** every time you log in — no terminal, no manual command.

### ✅ Requirements

* Linux with GNOME / Pop!_OS / Ubuntu
* Python 3 installed
* Discord installed and set to **start on login**

---

### 🔧 Step 1: Create an autostart entry

Open a terminal and run:

```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/dayflow-rpc.desktop
```

Paste the following **exactly** (edit the path if needed):

```ini
[Desktop Entry]
Type=Application
Name=DayFlowRPC
Exec=/usr/bin/python3 /home/<YOUR_USERNAME>/DayFlowRPC/dayflowrpc.py
X-GNOME-Autostart-enabled=true
```

Replace `<YOUR_USERNAME>` with your Linux username.

---

### 💾 Step 2: Save and exit nano

* Press **Ctrl + O** → Enter (save)
* Press **Ctrl + X** (exit)

---

### ✅ Step 3: Test manually (recommended)

Before logging out, test once:

```bash
/usr/bin/python3 /home/<YOUR_USERNAME>/DayFlowRPC/dayflowrpc.py
```

If Discord is open and the presence appears, autostart will work.

---

### 🔁 Step 4: Activate autostart

Log out and log back in:

```bash
gnome-session-quit --logout
```

After login:

* Open Discord
* Wait ~1–2 minutes
* Your Rich Presence should appear automatically 🎯

---

### 🧠 Notes

* This **does NOT start Discord** — Discord should already be set to start on login.
* If Discord opens later, the script will still connect once Discord is running.
* The script runs safely using Discord’s **Rich Presence (IPC)** — no tokens, no self-botting.

---

### 🛠 Optional Improvements

* Add retry logic if Discord isn’t open yet
* Convert to a `systemd --user` service for auto-restart
* Sync modes with Google Calendar

---

### ✅ Result

Once set up, **DayFlowRPC becomes part of your system**, running silently and reflecting your daily rhythm automatically.

---

🕯️ Final Note
This project isn’t about productivity or automation alone.

It’s about using code to reduce unnecessary worry, improve clarity, and make daily life a little calmer for both myself and the people close to me.
