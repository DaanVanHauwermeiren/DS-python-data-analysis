heatmap_prep = survey_data.groupby([survey_data['eventDate'].dt.year, survey_data['eventDate'].dt.month]).size().unstack()