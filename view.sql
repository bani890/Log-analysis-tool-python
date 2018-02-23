create view path_hits as select substr(log.path, 10) as slughit, count(path) as hits from log group by path order by hits desc; 
create view auth_slug_hit as select author,title, hits from articles,path_hits where articles.slug=path_hits.slughit;
create view error_table as select date(time), count(*) as error_hits from log where status='404 NOT FOUND' group by date(time) order by date(time);
create view all_views as select date(time), count(*) as views from log group by date(time) order by date(time);
