# alarms-transformations

An **ETL pipeline** script built in **Python**, designed to process alarm data stored in a text file and prepare it for insertion into a PostgreSQL database. This script is ideal for transforming raw logs into structured tabular formats for analysis, ingestion, or monitoring systems.

---

## Technologies Used

- **Language**: Python 3
- **Storage Input**: Flat text file (`alarms.txt`)
- **ETL Script**: `transform.py`
- **Target DB**: PostgreSQL
- **Visualization**: DBeaver (for local database preview)

---


##  PostgreSQL Output Preview

The transformed alarm data was tested and successfully loaded into a PostgreSQL database. The screenshots below show how the structured data appears in **DBeaver**:

![image](https://github.com/user-attachments/assets/e18166fa-f8bd-4e49-8ffa-0e1b53102eb5)
![image](https://github.com/user-attachments/assets/b9c9d7c0-82b3-47e1-8751-f8b38f57a321)
 *The code still needs some organizing — just ran out of time. But it has been tested locally.*

---

##  How to Run

1. Ensure you have Python 3 installed.
2. Place the raw alarm data in `alarms.txt`.
3. Run the transformation script:

```bash
python transform.py


