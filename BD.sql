create table Traffic_light ( Id_light Int(3), Car_count_full_run Int(11),
Car_average_in_minute Int(11), Count_color_swithes Int(11), Primary key (Id_light));
create table Car_stats ( Car_id Int(3), Car_spawn_ticks Int(11),
Car_exit_ticks Int(11), Primary key (Car_id));