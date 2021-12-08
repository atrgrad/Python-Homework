{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "abf2890f-e5ae-4141-9961-94c5b1456940",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import CSV file\n",
    "\n",
    "from pathlib import Path\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bdddf764-1092-4520-9ea3-f4af7a7f8af0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the file path\n",
    "\n",
    "csvpath = Path(\"../PyBank/resources/budget_data.csv\")\n",
    "output_file = Path(\"../PyBank/analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fd8a787c-76ca-4c07-8a17-f43fcf235a01",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define lists and variables needed\n",
    "\n",
    "pnl_changes = []\n",
    "month_changes = []\n",
    "increase = [\"\",0]\n",
    "decrease = [\"\",99999999999999]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5607789c-a5ab-4e03-9df1-3199e7ec5ebb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define functions\n",
    "def total_months(csvpath):\n",
    "    with open(csvpath) as x:\n",
    "        next(x)\n",
    "        row_count = sum(1 for line in x)\n",
    "        return(row_count)\n",
    "    \n",
    "def total_pnl(csvpath):\n",
    "    with open(csvpath) as y:\n",
    "        next(y)\n",
    "        total = 0\n",
    "        for row in csv.reader(y):\n",
    "            total += int(row[1])\n",
    "        return(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5b62e186-a208-4df7-9700-861e21255090",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Average P&L, Max & Min Change\n",
    "\n",
    "with open(csvpath, 'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    \n",
    "    header = next(csvreader)\n",
    "            \n",
    "    init_pnl = int(row[1])\n",
    "    count = -1\n",
    "    \n",
    "    for row in csvreader:\n",
    "        change = int(row[1]) - init_pnl\n",
    "        init_pnl = int(row[1])\n",
    "        pnl_changes = pnl_changes + [change]\n",
    "        month_changes = month_changes + [row[0]]\n",
    "        count = count + 1\n",
    "        \n",
    "        if change > increase[1]:\n",
    "            increase[0] = row[0]\n",
    "            increase[1] = change\n",
    "            \n",
    "        if change < decrease[1]:\n",
    "            decrease[0] = row[0]\n",
    "            decrease[1] = change"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b3961e57-700c-40c7-a5ec-4a18919aafd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate average and define variables for functions\n",
    "\n",
    "average = round(sum(pnl_changes) / (count),2)\n",
    "tm = total_months(csvpath)\n",
    "pnl = total_pnl(csvpath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9a5ccc74-d3de-4f13-9dc8-2d68fa0a177b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize output variable\n",
    "\n",
    "output = (\n",
    "    f\"Financial Analysis\\n\"\n",
    "    f\"--------------------------------------------\\n\"\n",
    "    f\"Total Months: {tm}\\n\"\n",
    "    f\"Total: ${pnl}\\n\"\n",
    "    f\"Average Change: ${average}\\n\"\n",
    "    f\"Greatest Increase in Profits: {increase[0]} (${increase[1]})\\n\"\n",
    "    f\"Greatest Increase in Profits: {decrease[0]} (${decrease[1]})\\n\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bf7c62f5-a7ec-4e77-8645-33cc68fca08e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write output txt file\n",
    "\n",
    "with open(output_file, \"w\") as txt_file:\n",
    "    txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d71ef4ee-e83d-4d14-8076-8e8e67372b32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "--------------------------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Increase in Profits: Sep-2013 ($-2196167)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Print output of financial analysis\n",
    "\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0946e470-dd2c-437a-a1ca-12eef8f5100a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
