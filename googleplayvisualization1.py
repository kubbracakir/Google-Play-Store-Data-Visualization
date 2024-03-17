import pandas as pd
df = pd.read_csv('/Users/mac/Desktop/Python/src/datascience/datavisualization/1/googleplaystore.csv')
df.head()
df.columns
df.columns = df.columns.str.replace(" ","_")
df.columns
df.shape
df.dtypes
df.isnull().sum()
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
sns.set(rc={"figure.dpi":300, "figure.figsize":(12,9)})
sns.heatmap(df.isnull(), cbar=False)

rating_median = df["Rating"].median()
print(rating_median)
df["Rating"].fillna(rating_median, inplace=True)


df.dropna(inplace=True)
df.isnull().sum().sum()
df.info()
df["Reviews"].describe()
df["Reviews"] = df["Reviews"].astype("int64")
df["Reviews"].describe().round()
print(len(df["Size"].unique()))
df["Size"].unique()
df["Size"].replace("M","", regex=True, inplace = True)
df["Size"].replace("k","", regex=True, inplace = True)
df["Size"].unique()
size_median = df[df["Size"]!="Varies with device"]["Size"].astype(float).median()
size_median
df["Size"].replace("Varies with device", size_median, inplace=True)
df.Size = pd.to_numeric(df.Size)
df.Size.head()
df.Size.describe().round()
df["Installs"].unique()
df.Installs = df.Installs.apply(lambda x:x.replace("+",""))
df.Installs = df.Installs.apply(lambda x:x.replace(",",""))
df.Installs = df.Installs.apply(lambda x:int(x))
df["Installs"].unique()
df["Price"].unique()
df.Price = df.Price.apply(lambda x:x.replace("$",""))
df.Price = df.Price.apply(lambda x:float(x))
df["Price"].unique()
len(df["Genres"].unique())
df["Genres"].head(10)
df["Genres"] = df["Genres"].str.split(";").str[0]
len(df["Genres"].unique())
df["Genres"].unique()
df["Genres"].value_counts()
df["Genres"].replace("Music & Audio", "Music", inplace =True)
df["Last_Updated"].head()
df["Last_Updated"] = pd.to_datetime(df["Last_Updated"])
df.head()
df.dtypes
df["Type"].value_counts().plot(kind="bar", color ="red")
plt.title("Free & Paid")
sns.boxplot(x = "Type", y = "Rating", data = df)
plt.title("Content rating with their counts")
sns.countplot(y = "Content_Rating", data = df)
plt.title("Content rating with their counts")
sns.boxplot(x = "Content_Rating", y = "Rating", data = df)
plt.title("The content rating & rating", size=20)
cat_num = df["Category"].value_counts()
sns.barplot(x = cat_num, y = cat_num.index, data = df)
plt.title("The number of categories", size=20)
sns.scatterplot(data = df, y = "Category", x = "Price")
plt.title("Category & Price", size=20)
sns.heatmap(df.corr(), annot = True, linewidths=.5, fmt=".2f")
plt.title("Heatmap for numerical columns", size=20)
sns.histplot(df["Rating"], kde = True)
plt.title("Histogram with the kde for the rating column ", size=20,)
