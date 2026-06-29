# Metadata Changes Report for 100-Year Stations

> [!IMPORTANT]
> **Data Homogenization & Parallel Measurements**
> 
> When the experimental design of a weather station changes (e.g., transitioning to automated sensors), meteorological institutes conduct **Parallel Measurements** (*Parallelmessungen*). The new and old instruments are run simultaneously for 1-2 years to statistically isolate the exact bias between them.
> 
> * **Raw Historical Data:** The dataset used in this repository relies on the DWD's public, unadjusted raw historical data. It contains the exact original observations, meaning it inherently includes the structural biases introduced by these experimental shifts. 
> * **Raw Parallel Data Unavailability:** The raw, minute-by-minute parallel measurement logs required to manually calculate the exact sensor bias are retained in internal DWD research archives and are **not** available in the standard public Open Data portal used here.
> * **Homogenized Data:** For official climate change tracking, the DWD applies mathematical offsets derived from those internal parallel measurements to the raw data. This creates a "homogenized dataset" where experimental design shifts are mathematically smoothed out.

> [!NOTE]
> **Understanding Experimental Design Shifts & Data Implications**
> 
> * **Calculation Methodology (`Berechnungs_Methode`) & The MIRAKEL System (2001):** 
>   * *Shift:* Historically, before this architectural change was enforced, a human observer checked the temperature 3 times a day at fixed local times (e.g., 07:00, 14:00, and 21:00) and the daily mean was calculated using a weighted formula. In 2001, the DWD introduced a new central IT database system called **MIRAKEL**. With this modernization, temperature is now measured continuously, and the modern protocol determines the daily mean based on a true mathematical average of 24 continuous hourly measurements.
>   * *Data Implication:* Transitioning from a weighted 3-point approximation to a true 24-hour average can introduce an artificial step-change in long-term `Mean_Temp_C` time series, as the two mathematical approaches yield slightly different baselines for the exact same weather.
> 
> * **Reporting System and Automation:** 
>   * *Shift:* Historical climate data was recorded manually by human observers into physical climate diaries. Under the modern system (fully integrating into MIRAKEL from 2001 onwards), climate records are automatically extracted directly from the real-time, digital SYNOP (Synoptic) weather reporting pipeline.
>   * *Data Implication:* While full automation drastically reduces human error, the sudden removal of human smoothing and the shift to raw digital pipelines can alter the variance and consistency of the historical dataset.
> 
> * **24-Hour Measurement Window Boundaries:** 
>   * *Shift:* The temporal definition of a "day" for measurement purposes shifted. Historically, the 24-hour measurement window often concluded at a specific local evening time (e.g., resetting at 21:30 local time). Automated SYNOP reporting shifted this boundary to align with midnight UTC.
>   * *Data Implication:* This boundary shift can cause extreme events (like a late evening heatwave or an overnight freeze) to be recorded on a different calendar day than they would have been historically. This slightly alters the day-to-day distribution of extreme values.
> 
> * **Sensor Hardware (`Sensor_Typ`):** 
>   * *Shift:* Historically, maximum and minimum temperatures were determined using specialized physical glass thermometers: a mercury maximum thermometer (which uses a constriction to prevent the mercury from falling until manually shaken down) and an alcohol minimum thermometer (where a small index is dragged to the lowest point by the surface tension and stays there). A human observer manually read these extremes once a day (typically during the evening observation) and then physically reset the instruments for the next 24 hours. Modern temperature data is recorded using electronic digital sensors (such as the PT100) that sample the air continuously, automatically logging the exact absolute extremes over the day.
>   * *Data Implication:* Because **digital sensors react almost instantly to brief environmental fluctuations, automated stations tend to capture wider extremes**. This introduces a slight systemic upward bias in absolute maximum temperatures (`Max_Temp_C`) and a slight downward bias in absolute minimum temperatures (`Min_Temp_C`) compared to the sluggish responses of historical glass instruments.
> 
> * **Observation Setup and Human Reliability:** 
>   * *Shift:* Historically, physical glass thermometers were mounted at a standard height of 2 meters and were predominantly read and maintained by amateur volunteer observers (such as teachers, farmers, or local officials). Today, modern stations operate fully autonomously without daily human intervention.
>   * *Data Implication:* Relying on human observers introduced vulnerabilities absent in modern automated data. Reading a glass meniscus at a 2-meter height could easily introduce parallax errors depending on the observer's eye level. Furthermore, amateur observers might have occasionally sent untrained proxies (like family members) to take readings, or retrospectively guessed/imputed missing data if they were sick or away on holiday for a while, potentially impacting the consistency of the historical record.
> 
> ---
> **Scientific Sources & DWD Documentation:**
> * *Parallelmessungen an deutschen Klimareferenzstationen: Schlussfolgerungen im Hinblick auf Homogenität und Messunsicherheiten* (Berichte des Deutschen Wetterdienstes, Band 253, 2020)
> * *Kaspar, F. et al. (2016): Beobachtung von Klima und Klimawandel in Mitteleuropa und Deutschland.* (Details the transition from "Mannheimer Stunden" to automated 24-hour mean methodologies)
> * *DWD Climate Data Center (CDC) Open Data Portal Documentation:* (Verifies that raw high-resolution parallel measurement logs used for internal mathematical homogenization are excluded from the public historical archives to prevent statistical misinterpretation).


| Station ID | Station Name | Date of Change | Attribute | New Value |
|---|---|---|---|---|
| 00003 | Aachen | 1904-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00003 | Aachen | 1905-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00003 | Aachen | 1944-09-01 | Sensor_Typ | None |
| 00003 | Aachen | 1944-09-01 | Strahlungsschutz | None |
| 00003 | Aachen | 1945-04-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00003 | Aachen | 1945-04-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 00003 | Aachen | 1993-07-01 | Sensor_Typ | PT 100 (Luft) |
| 00003 | Aachen | 1993-07-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00003 | Aachen | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00164 | Angermünde | 1936-03-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00164 | Angermünde | 1936-03-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 00164 | Angermünde | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 00164 | Angermünde | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 00164 | Angermünde | 1987-12-01 | Sensor_Typ | PT 100 (Luft) |
| 00164 | Angermünde | 1987-12-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00164 | Angermünde | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00164 | Angermünde | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00186 | Arnsberg | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00186 | Arnsberg | 1946-06-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00186 | Arnsberg | 1947-01-01 | Berechnungs_Methode | None |
| 00186 | Arnsberg | 1947-01-02 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00320 | Heinersreuth-Vollhof | 1901-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00320 | Heinersreuth-Vollhof | 1943-04-01 | Sensor_Typ | None |
| 00320 | Heinersreuth-Vollhof | 1943-04-01 | Strahlungsschutz | None |
| 00320 | Heinersreuth-Vollhof | 1946-11-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00320 | Heinersreuth-Vollhof | 1946-11-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 00320 | Heinersreuth-Vollhof | 1947-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00320 | Heinersreuth-Vollhof | 2006-07-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00320 | Heinersreuth-Vollhof | 2006-07-01 | Sensor_Typ | PT 100 (Luft) |
| 00320 | Heinersreuth-Vollhof | 2006-07-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00691 | Bremen | 1991-06-19 | Sensor_Typ | PT 100 (Luft) |
| 00691 | Bremen | 1991-06-19 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00691 | Bremen | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00691 | Bremen | 2023-09-12 | Sensor_Typ | None |
| 00691 | Bremen | 2023-09-12 | Strahlungsschutz | None |
| 00691 | Bremen | 2023-09-18 | Sensor_Typ | PT 100 (Luft) |
| 00691 | Bremen | 2023-09-18 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00722 | Brocken | 1947-09-11 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 00722 | Brocken | 1947-09-11 | Sensor_Typ | None |
| 00722 | Brocken | 1947-09-11 | Strahlungsschutz | None |
| 00722 | Brocken | 1947-09-12 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00722 | Brocken | 1947-09-12 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 00722 | Brocken | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 00722 | Brocken | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00722 | Brocken | 1997-06-04 | Sensor_Typ | PT 100 (Luft) |
| 00722 | Brocken | 1997-06-04 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00722 | Brocken | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00853 | Chemnitz | 1883-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 20 MOZ und Tageswerte) |
| 00853 | Chemnitz | 1935-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00853 | Chemnitz | 1935-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00853 | Chemnitz | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 00853 | Chemnitz | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 00853 | Chemnitz | 1981-03-01 | Sensor_Typ | PT 100 (Luft) |
| 00853 | Chemnitz | 1981-03-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00853 | Chemnitz | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00853 | Chemnitz | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00853 | Chemnitz | 2025-04-02 | Sensor_Typ | None |
| 00853 | Chemnitz | 2025-04-02 | Strahlungsschutz | None |
| 00853 | Chemnitz | 2025-09-03 | Sensor_Typ | PT 100 (Luft) |
| 00853 | Chemnitz | 2025-09-03 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00863 | Clausthal-Zellerfeld | 1946-08-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00863 | Clausthal-Zellerfeld | 2007-09-12 | Sensor_Typ | PT 100 (Luft) |
| 00863 | Clausthal-Zellerfeld | 2007-09-12 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00863 | Clausthal-Zellerfeld | 2007-10-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00863 | Clausthal-Zellerfeld | 2012-03-29 | Sensor_Typ | None |
| 00863 | Clausthal-Zellerfeld | 2012-03-29 | Strahlungsschutz | None |
| 00880 | Cottbus | 1888-11-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00880 | Cottbus | 1888-11-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 00880 | Cottbus | 1888-11-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 00880 | Cottbus | 1946-06-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 00880 | Cottbus | 1951-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 00880 | Cottbus | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 00880 | Cottbus | 1988-08-10 | Sensor_Typ | PT 100 (Luft) |
| 00880 | Cottbus | 1988-08-10 | Strahlungsschutz | Temperaturmessung, elektr. |
| 00880 | Cottbus | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 00880 | Cottbus | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 00919 | Darmstadt-Botanischer Garten | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 00919 | Darmstadt-Botanischer Garten | 1937-02-03 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01358 | Fichtelberg | 1904-04-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 01358 | Fichtelberg | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 01358 | Fichtelberg | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 01358 | Fichtelberg | 1973-01-01 | Sensor_Typ | PT 100 (Luft) |
| 01358 | Fichtelberg | 1973-01-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 01358 | Fichtelberg | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01358 | Fichtelberg | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 01425 | Frankfurt/Main (Feldbergstr.) | 1854-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  06, 14, 22 MOZ und Tageswerte) |
| 01425 | Frankfurt/Main (Feldbergstr.) | 1870-01-29 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 01425 | Frankfurt/Main (Feldbergstr.) | 1870-01-29 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 01425 | Frankfurt/Main (Feldbergstr.) | 1893-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01526 | Fulda-Horas | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 01526 | Fulda-Horas | 1920-11-01 | Sensor_Typ | None |
| 01526 | Fulda-Horas | 1920-11-01 | Strahlungsschutz | None |
| 01526 | Fulda-Horas | 1921-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 01526 | Fulda-Horas | 1921-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 01526 | Fulda-Horas | 1949-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01526 | Fulda-Horas | 2004-11-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 01526 | Fulda-Horas | 2004-11-01 | Sensor_Typ | PT 100 (Luft) |
| 01526 | Fulda-Horas | 2004-11-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 01580 | Geisenheim | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 01580 | Geisenheim | 1935-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01580 | Geisenheim | 2006-12-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 01580 | Geisenheim | 2006-12-01 | Sensor_Typ | PT 100 (Luft) |
| 01580 | Geisenheim | 2006-12-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 01684 | Görlitz | 1861-04-01 | Sensor_Typ | Thermometrograph |
| 01684 | Görlitz | 1880-01-01 | Sensor_Typ | None |
| 01684 | Görlitz | 1880-01-01 | Strahlungsschutz | None |
| 01684 | Görlitz | 1887-10-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 01684 | Görlitz | 1887-10-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 01684 | Görlitz | 1887-10-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 01684 | Görlitz | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 01684 | Görlitz | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 01684 | Görlitz | 1990-10-30 | Sensor_Typ | PT 100 (Luft) |
| 01684 | Görlitz | 1990-10-30 | Strahlungsschutz | Temperaturmessung, elektr. |
| 01684 | Görlitz | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01684 | Görlitz | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 01691 | Göttingen | 1871-04-01 | Sensor_Typ | Thermometrograph |
| 01691 | Göttingen | 1871-04-01 | Strahlungsschutz | Temperaturmessung, konv. |
| 01691 | Göttingen | 1884-01-01 | Sensor_Typ | None |
| 01691 | Göttingen | 1884-01-01 | Strahlungsschutz | None |
| 01691 | Göttingen | 1890-06-16 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 01691 | Göttingen | 1890-06-16 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 01691 | Göttingen | 1947-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01691 | Göttingen | 1993-11-10 | Sensor_Typ | PT 100 (Luft) |
| 01691 | Göttingen | 1993-11-10 | Strahlungsschutz | Temperaturmessung, elektr. |
| 01691 | Göttingen | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 01762 | Greiz-Dölau | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01891 | Rheda-Wiedenbrück-Lintel | 1938-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 01891 | Rheda-Wiedenbrück-Lintel | 1947-10-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 01960 | Halle (Stadt) | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 01960 | Halle (Stadt) | 1900-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 01960 | Halle (Stadt) | 1967-01-01 | Berechnungs_Methode | None |
| 02290 | Hohenpeißenberg | 1841-09-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02290 | Hohenpeißenberg | 1841-09-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02290 | Hohenpeißenberg | 1879-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 20 MOZ und Tageswerte) |
| 02290 | Hohenpeißenberg | 1901-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02290 | Hohenpeißenberg | 1993-12-09 | Sensor_Typ | PT 100 (Luft) |
| 02290 | Hohenpeißenberg | 1993-12-09 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02290 | Hohenpeißenberg | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02444 | Jena (Sternwarte) | 1824-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02444 | Jena (Sternwarte) | 1878-07-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02444 | Jena (Sternwarte) | 1878-07-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02444 | Jena (Sternwarte) | 1901-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 02444 | Jena (Sternwarte) | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02444 | Jena (Sternwarte) | 2004-08-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02444 | Jena (Sternwarte) | 2004-08-01 | Sensor_Typ | PT 100 (Luft) |
| 02444 | Jena (Sternwarte) | 2004-08-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02486 | Kaiserslautern | 2005-03-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02486 | Kaiserslautern | 2005-03-01 | Sensor_Typ | PT 100 (Luft) |
| 02486 | Kaiserslautern | 2005-03-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02522 | Karlsruhe | 1996-07-25 | Sensor_Typ | PT 100 (Luft) |
| 02522 | Karlsruhe | 1996-07-25 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02522 | Karlsruhe | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02532 | Kassel | 1881-04-01 | Sensor_Typ | Stationsthermometer |
| 02532 | Kassel | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02532 | Kassel | 1890-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02532 | Kassel | 1890-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02532 | Kassel | 1904-01-01 | Sensor_Typ | Stationsthermometer |
| 02532 | Kassel | 1904-01-01 | Strahlungsschutz | Temperaturmessung, konv. |
| 02532 | Kassel | 1904-10-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02532 | Kassel | 1904-10-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02532 | Kassel | 1938-10-07 | Sensor_Typ | Stationsthermometer |
| 02532 | Kassel | 1938-10-07 | Strahlungsschutz | Temperaturmessung, konv. |
| 02532 | Kassel | 1944-12-30 | Berechnungs_Methode | None |
| 02532 | Kassel | 1951-05-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02532 | Kassel | 1951-05-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02532 | Kassel | 1951-05-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02532 | Kassel | 2000-04-18 | Sensor_Typ | PT 100 (Luft) |
| 02532 | Kassel | 2000-04-18 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02532 | Kassel | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02578 | Kirchdorf/Poel | 1876-10-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 22 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1876-11-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 21 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1880-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  06, 14, 22 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1881-06-28 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1882-07-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  06, 14, 22 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1882-09-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1883-06-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  06, 14, 22 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1883-09-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02578 | Kirchdorf/Poel | 1955-08-01 | Sensor_Typ | Stationsthermometer |
| 02578 | Kirchdorf/Poel | 1955-08-01 | Strahlungsschutz | Temperaturmessung, konv. |
| 02578 | Kirchdorf/Poel | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02578 | Kirchdorf/Poel | 1992-05-07 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02578 | Kirchdorf/Poel | 1992-05-07 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02578 | Kirchdorf/Poel | 2004-07-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02578 | Kirchdorf/Poel | 2004-07-01 | Sensor_Typ | PT 100 (Luft) |
| 02578 | Kirchdorf/Poel | 2004-07-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02629 | Kleve | 1947-11-11 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02629 | Kleve | 2004-07-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02629 | Kleve | 2004-07-01 | Sensor_Typ | PT 100 (Luft) |
| 02629 | Kleve | 2004-07-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02928 | Leipzig-Holzhausen | 1825-03-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02928 | Leipzig-Holzhausen | 1825-03-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02928 | Leipzig-Holzhausen | 1870-06-01 | Sensor_Typ | Thermograph, unbekannt |
| 02928 | Leipzig-Holzhausen | 1870-06-01 | Strahlungsschutz | Temperaturmessung, konv. |
| 02928 | Leipzig-Holzhausen | 1883-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 20 MOZ und Tageswerte) |
| 02928 | Leipzig-Holzhausen | 1884-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 02928 | Leipzig-Holzhausen | 1884-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 02928 | Leipzig-Holzhausen | 1901-07-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02928 | Leipzig-Holzhausen | 1951-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 02928 | Leipzig-Holzhausen | 1959-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 02928 | Leipzig-Holzhausen | 1962-08-01 | Berechnungs_Methode | None |
| 02928 | Leipzig-Holzhausen | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 02928 | Leipzig-Holzhausen | 1990-04-01 | Sensor_Typ | PT 100 (Luft) |
| 02928 | Leipzig-Holzhausen | 1990-04-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 02928 | Leipzig-Holzhausen | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 02928 | Leipzig-Holzhausen | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 02928 | Leipzig-Holzhausen | 2019-06-23 | Sensor_Typ | None |
| 02928 | Leipzig-Holzhausen | 2019-06-23 | Strahlungsschutz | None |
| 02928 | Leipzig-Holzhausen | 2019-06-27 | Sensor_Typ | PT 100 (Luft) |
| 02928 | Leipzig-Holzhausen | 2019-06-27 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03015 | Lindenberg | 1945-08-01 | Sensor_Typ | None |
| 03015 | Lindenberg | 1945-08-01 | Strahlungsschutz | None |
| 03015 | Lindenberg | 1946-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 03015 | Lindenberg | 1946-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 03015 | Lindenberg | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 03015 | Lindenberg | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 03015 | Lindenberg | 1976-11-28 | Sensor_Typ | PT 100 (Luft) |
| 03015 | Lindenberg | 1976-11-28 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03015 | Lindenberg | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03015 | Lindenberg | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03126 | Magdeburg | 1894-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 03126 | Magdeburg | 1920-01-01 | Sensor_Typ | None |
| 03126 | Magdeburg | 1920-01-01 | Strahlungsschutz | None |
| 03126 | Magdeburg | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 03126 | Magdeburg | 1947-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 03126 | Magdeburg | 1947-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 03126 | Magdeburg | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 03126 | Magdeburg | 1979-01-01 | Sensor_Typ | PT 100 (Luft) |
| 03126 | Magdeburg | 1979-01-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03126 | Magdeburg | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03126 | Magdeburg | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03196 | Marnitz | 1947-05-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 03196 | Marnitz | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 03196 | Marnitz | 1977-01-01 | Sensor_Typ | PT 100 (Luft) |
| 03196 | Marnitz | 1977-01-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03196 | Marnitz | 1991-11-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 03196 | Marnitz | 1992-12-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03196 | Marnitz | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03537 | Neumünster | 1936-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03537 | Neumünster | 1947-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 03537 | Neumünster | 1990-08-01 | Sensor_Typ | None |
| 03537 | Neumünster | 1990-08-01 | Strahlungsschutz | None |
| 03537 | Neumünster | 1990-09-11 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 03537 | Neumünster | 1990-09-11 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 03631 | Norderney | 1897-09-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 03631 | Norderney | 1947-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03631 | Norderney | 1993-09-15 | Sensor_Typ | PT 100 (Luft) |
| 03631 | Norderney | 1993-09-15 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03631 | Norderney | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03730 | Oberstdorf | 1936-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03730 | Oberstdorf | 1994-07-17 | Sensor_Typ | PT 100 (Luft) |
| 03730 | Oberstdorf | 1994-07-17 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03730 | Oberstdorf | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03946 | Plauen | 1883-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  08, 14, 20 MOZ und Tageswerte) |
| 03946 | Plauen | 1887-06-11 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 03946 | Plauen | 1887-06-11 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 03946 | Plauen | 1921-01-01 | Berechnungs_Methode | None |
| 03946 | Plauen | 1935-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 03946 | Plauen | 1945-04-05 | Berechnungs_Methode | None |
| 03946 | Plauen | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 03946 | Plauen | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 03946 | Plauen | 1982-10-14 | Sensor_Typ | PT 100 (Luft) |
| 03946 | Plauen | 1982-10-14 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03946 | Plauen | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03946 | Plauen | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 03946 | Plauen | 2023-10-07 | Sensor_Typ | None |
| 03946 | Plauen | 2023-10-07 | Strahlungsschutz | None |
| 03946 | Plauen | 2023-10-10 | Sensor_Typ | PT 100 (Luft) |
| 03946 | Plauen | 2023-10-10 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03987 | Potsdam | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 03987 | Potsdam | 1978-03-01 | Sensor_Typ | PT 100 (Luft) |
| 03987 | Potsdam | 1978-03-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 03987 | Potsdam | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 03987 | Potsdam | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 04024 | Putbus | 1853-09-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 04024 | Putbus | 1853-09-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 04024 | Putbus | 1853-11-01 | Sensor_Typ | Thermometrograph |
| 04024 | Putbus | 1853-11-01 | Strahlungsschutz | Temperaturmessung, konv. |
| 04024 | Putbus | 1879-05-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 04024 | Putbus | 1879-05-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 04024 | Putbus | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 04024 | Putbus | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 04024 | Putbus | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 04024 | Putbus | 1974-01-01 | Sensor_Typ | None |
| 04024 | Putbus | 1974-01-01 | Strahlungsschutz | None |
| 04024 | Putbus | 1974-04-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 04024 | Putbus | 1974-04-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 04024 | Putbus | 1977-01-01 | Sensor_Typ | PT 100 (Luft) |
| 04024 | Putbus | 1977-01-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 04024 | Putbus | 1991-01-01 | Berechnungs_Methode | None |
| 04024 | Putbus | 1991-11-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 04024 | Putbus | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 04104 | Regensburg | 1901-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 04104 | Regensburg | 1947-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 04104 | Regensburg | 1962-06-26 | Sensor_Typ | None |
| 04104 | Regensburg | 1962-06-26 | Strahlungsschutz | None |
| 04104 | Regensburg | 1962-06-27 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 04104 | Regensburg | 1962-06-27 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 04104 | Regensburg | 1994-03-15 | Sensor_Typ | PT 100 (Luft) |
| 04104 | Regensburg | 1994-03-15 | Strahlungsschutz | Temperaturmessung, elektr. |
| 04104 | Regensburg | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 04125 | Reichenhall, Bad | 1945-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 04125 | Reichenhall, Bad | 1948-10-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 04625 | Schwerin | 1942-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 04625 | Schwerin | 1946-07-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 04625 | Schwerin | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 04625 | Schwerin | 1988-04-25 | Sensor_Typ | PT 100 (Luft) |
| 04625 | Schwerin | 1988-04-25 | Strahlungsschutz | Temperaturmessung, elektr. |
| 04625 | Schwerin | 1991-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 04625 | Schwerin | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 04748 | Sondershausen | 1887-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 04748 | Sondershausen | 1991-04-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 04748 | Sondershausen | 2004-11-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 04748 | Sondershausen | 2004-11-01 | Sensor_Typ | PT 100 (Luft) |
| 04748 | Sondershausen | 2004-11-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05099 | Trier-Zewen | 1935-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 05099 | Trier-Zewen | 1947-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05099 | Trier-Zewen | 2008-06-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 05099 | Trier-Zewen | 2008-06-01 | Sensor_Typ | PT 100 (Luft) |
| 05099 | Trier-Zewen | 2008-06-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05349 | Waren (Müritz) | 1899-07-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 05349 | Waren (Müritz) | 1947-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1949-1966, basierend auf den drei Klimaterminen (Termine  07, 14, 21 MOZ und Tageswerte) |
| 05349 | Waren (Müritz) | 1967-01-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine des eMD 1967-1990, Terminwerte basierend auf Daten der synoptischen Haupttermine (00,06,12,18 UTC) und Tageswerte, sowie Klimadaten nacherfasst im Rahmen des Projektes KLIDADIGI zu unterschiedlichen Zeiträumen. |
| 05349 | Waren (Müritz) | 1975-05-01 | Sensor_Typ | None |
| 05349 | Waren (Müritz) | 1975-05-01 | Strahlungsschutz | None |
| 05349 | Waren (Müritz) | 1977-05-01 | Sensor_Typ | PT 100 (Luft) |
| 05349 | Waren (Müritz) | 1977-05-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05349 | Waren (Müritz) | 1994-06-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05349 | Waren (Müritz) | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 05349 | Waren (Müritz) | 2008-05-09 | Sensor_Typ | None |
| 05349 | Waren (Müritz) | 2008-05-09 | Strahlungsschutz | None |
| 05349 | Waren (Müritz) | 2008-05-14 | Sensor_Typ | PT 100 (Luft) |
| 05349 | Waren (Müritz) | 2008-05-14 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05349 | Waren (Müritz) | 2014-07-08 | Sensor_Typ | None |
| 05349 | Waren (Müritz) | 2014-07-08 | Strahlungsschutz | None |
| 05349 | Waren (Müritz) | 2014-07-10 | Sensor_Typ | PT 100 (Luft) |
| 05349 | Waren (Müritz) | 2014-07-10 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05440 | Weißenburg-Emetzheim | 1901-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 05440 | Weißenburg-Emetzheim | 1936-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05440 | Weißenburg-Emetzheim | 1993-05-01 | Sensor_Typ | PT 100 (Luft) |
| 05440 | Weißenburg-Emetzheim | 1993-05-01 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05440 | Weißenburg-Emetzheim | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |
| 05498 | Wertheim-Eichel | 1947-07-10 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05498 | Wertheim-Eichel | 1947-07-10 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 05498 | Wertheim-Eichel | 1983-10-01 | Sensor_Typ | None |
| 05498 | Wertheim-Eichel | 1983-10-01 | Strahlungsschutz | None |
| 05498 | Wertheim-Eichel | 1983-11-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 05498 | Wertheim-Eichel | 1983-11-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 05732 | Wrixum/Föhr | 1938-01-01 | Berechnungs_Methode | None |
| 05732 | Wrixum/Föhr | 1938-01-01 | Sensor_Typ | Psychrometerthermometer (trocken) |
| 05732 | Wrixum/Föhr | 1938-01-01 | Strahlungsschutz | Temperatur/Feuchtemessung, konv. |
| 05732 | Wrixum/Föhr | 1941-01-01 | Berechnungs_Methode | KLIDADIGI: Klimadaten nacherfasst (3 Termine:  07, 14, 21 MOZ und Tageswerte) |
| 05732 | Wrixum/Föhr | 1947-09-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05792 | Zugspitze | 1901-01-01 | Berechnungs_Methode | Klimadaten aus Klimaroutine des DWD (3 Termine: um  07, 14, 21 MOZ, ab 01.01.1987 07:30,14:30,21:30 MEZ) und Tageswerte jeweils nach Beobachteranleitung für Klimastationen (BAK) |
| 05792 | Zugspitze | 1986-03-13 | Sensor_Typ | PT 100 (Luft) |
| 05792 | Zugspitze | 1986-03-13 | Strahlungsschutz | Temperaturmessung, elektr. |
| 05792 | Zugspitze | 2001-04-01 | Berechnungs_Methode | Klimadaten aus der Klimaroutine nach 1.4.2001, generiert aus SYNOP-Meldungen (3 Termine 06, 12, 18 UTC und Tageswerte aus stündlichen Werten oder Beobachtungen an Hauptterminen) |