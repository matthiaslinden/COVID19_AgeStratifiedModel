# Overview
Both SurvStat@RKI2.0 and the Dashboard's database contain infor weather a specific case (better: group of cases) on a reporting-date developed symptoms or not. Whereas Survstat@RKI2.0 only tells how many cases in each Age-group (1-year groups up to 80 and 80+) that were reported within a week (symptomatic,asymptomatic,unknown), the dashboard's database contains precise dates for reporting and symptom-onset for 6 wider age-groups. In case the date of symptom-onset is unknown or in case of asymptomatic, the dashboard's database contains a '0' in the 'ist_Erkrankungsbegin'-row.

## Quality of reporting
Some Landkreise report mostly symptomatic ('ist_Erkrankungsbegin'==1) others mosty asymptomatic ('ist_Erkrankungsbeginn'==0), which might be an indication of different testing-strategies.
A non-neglible number of case_reports indicate symptom-onset == reporting_date. Some Lankreise mostly report this combination, which seems to not represent reality.

In other Landkreisen, the ratio of asymptomatic to symptomatic changes with time.

The transistion from mostly no symptomatic to mostly asymptomatic / unkown for a given Landkreis might be an indicator for how well the local TTI is working.