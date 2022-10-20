# Medical Premises
This project is a console application for the selection of premises for a medical institution according to the specified parameters. It is a **pet project** to get experience with **Python** and **MongoDB**.

With this application **you can**:
* View the available premises
* Add a premises to the table
* Set parameters for premises selection
* View the selected premises
## Requirements
* Python 3.10.8
* MongoDB Community Server 6.0.2
## Installation
**Step 1**. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community).

**Step 2**. Install [Python](https://www.python.org/downloads/).

**Step 3**. Install Python libraries.
For this application to work, you need to download several libraries. To install, use the pip package installer.
1. Install **pymongo** to work with MongoDB from Python.
```
pip install pymongo
```
2. Install **prettytable** to easily displaying tabular data in ASCII table format in Python.
```
pip install prettytable
```
**Step 4**. Clone this repository to your local computer.
```
git clone https://github.com/SpaceLacuna/medical-premises.git
```
## Running
Since this is a console application, you need to work on the command line.

**Step 1**. Run cmd.exe.

**Step 2**. Navigate to the root folder of this project.
```
cd ...\medical-premises
```
**Step 3**. Run file run.py.
```
python run.py
```
## Usage Example
If you did everything correctly, the following message will appear.

![Untitl11232ed](https://user-images.githubusercontent.com/115897935/196043646-ba1887ea-7c32-440a-8bb5-1e63fbc3a3ed.png)

Initially, you will have an empty table. Use point 2 to add a premises.

![Untitled](https://user-images.githubusercontent.com/115897935/196043964-ba30409a-be0d-4d12-a2df-40f3c74f6a61.png)

You have added some premises to the table. To see them all, use point 1.

![Untitled11111111](https://user-images.githubusercontent.com/115897935/196048380-cd654494-1f56-4b01-b4f3-bc62f32b6822.png)

If you need to select a room according to certain parameters, use point 4.

![Untitle1d](https://user-images.githubusercontent.com/115897935/196048331-11698b0a-edd7-4b84-a3f5-4384666581bf.png)

You can see the premises you have selected using the point 5.

![Untitled](https://user-images.githubusercontent.com/115897935/196048248-0b96a101-7b04-4f46-919a-00f00e36a645.png)

To remove a premises from the table, use point 3.

To close the application, use point 6.
