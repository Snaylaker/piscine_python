from datetime import date

start_date = date(1970, 1, 1)
today_seconds = (date.today()-start_date).total_seconds()

print("Seconds since January 1, 1970:",
      '{:,}'.format(today_seconds),
      " or  in scientific notation Oct 21 2022",
      '{:e}'.format(today_seconds),
      )
