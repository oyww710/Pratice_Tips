def _calculate_stats(input_path, output_path): """Calculates event statistics."""
events = pd.read_json(input_path) #D
stats = events.groupby(["date", "user"]).size().reset_index() #E
Path(output_path).parent.mkdir(exist_ok=True) #F stats.to_csv(output_path, index=False) #G

calculate_stats = PythonOperator( task_id="calculate_stats", python_callable=_calculate_stats, 
op_kwargs={
"input_path": "/data/events.json",
"output_path": "/data/stats.csv", },
dag=dag, )
