-- ALL Schemas --
select 'recompress schema ' || '"' || object_name || '"' || ' enforce; commit;' || ' reorganize schema ' || '"' || object_name || '"' || ' enforce; commit;' || ' flush statistics; commit;' as reorg_command
from EXA_DBA_OBJECT_SIZES
where object_type = 'SCHEMA'
and object_is_virtual = 'false'
order by mem_object_size,object_name;
