import sqlite3
import datetime
import random
import os

DB_PATH = 'neri.db'

def seed_database():
    if not os.path.exists(DB_PATH):
        print("Database not found. Run app.py first.")
        return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Get all users (or create one if none exist)
    c.execute("SELECT id FROM users")
    users = c.fetchall()

    if not users:
        from werkzeug.security import generate_password_hash
        print("No users found. Creating 'testuser'...")
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                  ('testuser', generate_password_hash('test1234')))
        user_id = c.lastrowid
        c.execute("INSERT INTO profession_stats (user_id) VALUES (?)", (user_id,))
        users = [(user_id,)]
    
    today = datetime.date.today()

    for user in users:
        uid = user[0]
        
        # 1. Add Physical Tasks & Goals (Real Life Problem: Sedentary Tech Lifestyle)
        physical_tasks = [
            "Morning Walk (30 mins at park)", 
            "Drink 3L Water (Hydration tracking)", 
            "Fix Posture Exercises (Neck & Back stretch)", 
            "Avoid Junk Food (Dietary Control)"
        ]
        for task in physical_tasks:
            # Check if task exists
            c.execute("SELECT id FROM tasks WHERE user_id=? AND title=? AND task_date=?", (uid, task, today.isoformat()))
            if not c.fetchone():
                c.execute("INSERT INTO tasks (user_id, title, task_date, is_completed) VALUES (?, ?, ?, ?)", 
                          (uid, task, today.isoformat(), random.choice([0, 1])))

        # 2. Add Profession Tasks (Real Life Problem: Balancing project work and upskilling)
        prof_tasks = [
            ("Fix memory leak in production server (Bug-fix)", "core"), 
            ("Review PR for new payment gateway integration", "core"), 
            ("Complete AWS Solutions Architect notes (Upskilling)", "career"), 
            ("Prepare slides for Sprint Retrospective", "core"),
            ("Solve 2 LeetCode Medium problems (Interview Prep)", "career")
        ]
        total_prof = len(prof_tasks)
        completed_prof = 0
        for title, cat in prof_tasks:
            status = random.choice([0, 1])
            if status: completed_prof += 1
            c.execute("SELECT id FROM profession_tasks WHERE user_id=? AND title=?", (uid, title))
            if not c.fetchone():
                try:
                    c.execute("INSERT INTO profession_tasks (user_id, title, task_date, is_completed, category) VALUES (?, ?, ?, ?, ?)", 
                              (uid, title, today.isoformat(), status, cat))
                except Exception:
                    # Fallback if category missing
                    c.execute("INSERT INTO profession_tasks (user_id, title, task_date, is_completed) VALUES (?, ?, ?, ?)", 
                              (uid, title, today.isoformat(), status))

        # Update profession_stats for the dashboard rings
        c.execute("UPDATE profession_stats SET completed_count=?, target_count=? WHERE user_id=?", (completed_prof, total_prof, uid))

        # 3. Add Finance Data (Real Life Expenses in INR equivalent amounts)
        categories = ["Food", "Transport", "Entertainment", "Utilities", "Shopping", "Investment"]
        expense_templates = {
            "Food": [("Swiggy/Zomato Lunch", 250), ("Groceries from D-Mart", 1200), ("Coffee at Cafe", 180)],
            "Transport": [("Uber commute to office", 350), ("Metro Card Recharge", 500), ("Petrol", 1000)],
            "Entertainment": [("Netflix Subscription", 499), ("Movie Tickets", 600)],
            "Utilities": [("Internet Bill", 899), ("Electricity", 1500)],
            "Shopping": [("Amazon - Desk accessories", 850), ("Myntra - T-shirts", 1200)],
            "Investment": [("SIP Deduction", 5000), ("Stock market dip buy", 2500)]
        }
        for i in range(7):
            date_str = (today - datetime.timedelta(days=i)).isoformat()
            c.execute("SELECT id FROM daily_finance WHERE user_id=? AND entry_date=?", (uid, date_str))
            if not c.fetchone():
                # Add 1-2 random realistic transactions per day
                for _ in range(random.randint(1, 2)):
                    cat = random.choice(categories)
                    desc, amt = random.choice(expense_templates[cat])
                    # Add some slight variation to amounts
                    amt = amt + random.randint(-50, 50) if amt > 100 else amt
                    c.execute("INSERT INTO daily_finance (user_id, entry_date, category, amount, notes) VALUES (?, ?, ?, ?, ?)",
                              (uid, date_str, cat, float(amt), desc))

        # 4. Add Reminders (Real Life Commitments)
        reminders = [("Call parents tonight", 0), ("Pay credit card bill before 5th", 1), ("Team sync at 11 AM", 1)]
        for title, is_done in reminders:
            c.execute("SELECT id FROM reminders WHERE user_id=? AND title=?", (uid, title))
            if not c.fetchone():
                c.execute("INSERT INTO reminders (user_id, title, reminder_date, is_done) VALUES (?, ?, ?, ?)",
                          (uid, title, today.isoformat(), is_done))
                          
        # Update daily activity completion
        try:
             # Use the recalculate_daily_activity logic from app.py loosely
             pass
        except Exception as e:
             pass

    conn.commit()
    conn.close()
    print("Database seeded with realistic dummy data successfully.")

if __name__ == "__main__":
    seed_database()
