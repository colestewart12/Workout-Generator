from flask import Flask, request, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name", "World")
    return f"<p>Hello, {name}!</p>"

@app.route("/workouts", methods=["GET", "POST"])
def render_workouts():
    bodypart = request.args.get("bodypart", "")
    workout_type = request.args.get("workout_type", "")
    level = request.args.get("level", "")
    equipment = request.args.getlist('equipment')

    level_categories = {
        "All": [""],
        "Beginner": ["Beginner"],
        "Intermediate": ["Intermediate"]
    }
    
    if request.method == "POST":
        bodypart = request.form.get("bodypart", "")
        workout_type = request.form.get("workout_type", "")
        level = request.form.get("level", "")
        equipment = request.form.getList("equipment")

    bodypart_categories = {
        "All": [""],
        "Arms": ["Triceps", "Biceps", "Forearms"],
        "Legs": ["Quadriceps", "Glutes", "Abductors", "Hamstrings", "Adductors", "Calves"],
        "Shoulders": ["Shoulders", "Neck"],
        "Back": ["Lower Back", "Middle Back", "Traps", "Lats"],
        "Chest": ["Chest"],
        "Core": ["Abdominals"]
    }

    where_clauses = []
    params = {
        "bodypart": f"%{bodypart}%"
    }

    order_by_clause = """
    ORDER BY random()
    limit 10
    """

    workout_type_categories = {
        "All": [""],
        "Strength": ["Strength"],
        "Cardio": ["Cardio"],
        "Stretching": ["Stretching"],
        "Plyometrics": ["Plyometrics"],
        "Powerlifting": ["Powerlifting"],
        "Olympic Weightlifting": ["Olympic Weightlifting"],
        "Strongman": ["Strongman"]
    }

    if equipment:
        equipment_where_clauses = []
        for i, eq in enumerate(equipment):
            param_name = f"equipment_{i}"
            equipment_where_clauses.append(f"w.equipment ILIKE %({param_name})s")
            params[param_name] = f"%{eq}%"
        equipment_where_clause = " OR ".join(equipment_where_clauses)
        where_clauses.append(f"({equipment_where_clause})")


    if level and level in level_categories:
        selected_level = level_categories[level]
        level_where_clauses = []
        for i, l in enumerate(selected_level):
            param_name = selected_level[i]
            level_where_clauses.append(f"w.level ILIKE %({param_name})s")
            params[param_name] = f"%{l}%"
        
        level_where_clause = " OR ".join(level_where_clauses)
        where_clauses.append(f"({level_where_clause})")

    if workout_type and workout_type in workout_type_categories:
        selected_workout_types = workout_type_categories[workout_type]
        workout_type_where_clauses = []
        for i, wt in enumerate(selected_workout_types):
            param_name = f"workout_type_{i}"
            workout_type_where_clauses.append(f"w.type ILIKE %({param_name})s")
            params[param_name] = f"%{wt}%"

        workout_type_where_clause = " OR ".join(workout_type_where_clauses)
        where_clauses.append(f"({workout_type_where_clause})")


    if bodypart and bodypart in bodypart_categories:
        selected_bodyparts = bodypart_categories[bodypart]
        bodypart_where_clauses = []
        for i, bp in enumerate(selected_bodyparts):
            param_name = selected_bodyparts[i]
            bodypart_where_clauses.append(f"w.bodypart ILIKE %({param_name})s")
            params[param_name] = f"%{bp}%"

        bodypart_where_clause = " OR ".join(bodypart_where_clauses)
        where_clauses.append(f"({bodypart_where_clause})")

    where_clause = ""
    if where_clauses:
        where_clause = "WHERE " + " AND ".join(where_clauses)


    query = f"""
    SELECT w.title AS title, w.descrip AS description, w.type AS type, w.bodypart AS body_part,
           w.equipment AS equipment, w.level AS level
    FROM workout w
    {where_clause}
    {order_by_clause}
    """

    
    with conn.cursor() as cur:
        cur.execute(query, params)
        results = list(cur.fetchall())

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render_template("workouts_table.html", workouts=results)

        return render_template("workouts.html",
                               show_table=True,
                               params=request.args,
                               workouts=results,
                               equipment=equipment
                               )
    