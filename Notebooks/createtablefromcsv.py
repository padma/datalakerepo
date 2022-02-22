{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Overview\n",
    "This notebook will show you how to create and query a table or DataFrame that you uploaded to DBFS. DBFS is a Databricks File System that allows you to store data for querying inside of Databricks. This notebook assumes that you have a file already inside of DBFS that you would like to read from.\n",
    "\n",
    "This notebook is written in Python so the default cell type is Python. However, you can use different languages by using the %LANGUAGE syntax. Python, Scala, SQL, and R are all supported."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# File location and type\n",
    "file_location = \"/FileStore/tables/Country_codes.csv\"\n",
    "file_type = \"csv\"\n",
    "\n",
    "# CSV options\n",
    "infer_schema = \"false\"\n",
    "first_row_is_header = \"true\"\n",
    "delimiter = \",\"\n",
    "\n",
    "# The applied options are for CSV files. For other file types, these will be ignored.\n",
    "df = spark.read.format(file_type) \\\n",
    "  .option(\"inferSchema\", infer_schema) \\\n",
    "  .option(\"header\", first_row_is_header) \\\n",
    "  .option(\"sep\", delimiter) \\\n",
    "  .load(file_location)\n",
    "\n",
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a view or table\n",
    "\n",
    "temp_table_name = \"Country_codes_csv\"\n",
    "\n",
    "df.createOrReplaceTempView(temp_table_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "\n",
    "/* Query the created temp table in a SQL cell */\n",
    "\n",
    "select * from `Country_codes_csv`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# With this registered as a temp view, it will only be available to this particular notebook. If you'd like other users to be able to query this table, you can also create a table from the DataFrame.\n",
    "# Once saved, this table will persist across cluster restarts as well as allow various users across different notebooks to query this data.\n",
    "# To do so, choose your table name and uncomment the bottom line.\n",
    "\n",
    "permanent_table_name = \"Country_codes_csv\"\n",
    "\n",
    "# df.write.format(\"parquet\").saveAsTable(permanent_table_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "show tables"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
