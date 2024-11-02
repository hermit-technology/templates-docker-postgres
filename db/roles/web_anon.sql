create role web_anon nologin;

grant usage on schema postgrest to web_anon;

grant select on {{ database }}.postgrest.accounts to web_anon;
grant select on {{ database }}.postgrest.users to web_anon;
grant select on {{ database }}.postgrest.user_resources to web_anon;
grant select on {{ database }}.postgrest.user_structures to web_anon;
grant select on {{ database }}.postgrest.user_units to web_anon;
grant select on {{ database }}.postgrest.structures to web_anon;
grant select on {{ database }}.postgrest.structure_resources to web_anon;
grant select on {{ database }}.postgrest.resources to web_anon;
grant select on {{ database }}.postgrest.structure_factions to web_anon;
grant select on {{ database }}.postgrest.units to web_anon;
grant select on {{ database }}.postgrest.unit_factions to web_anon;
grant select on {{ database }}.postgrest.factions to web_anon;
grant select on {{ database }}.postgrest.unit_resources to web_anon;
