import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/diabetes.csv")

# -------------------------------
# Basic Information
# -------------------------------
print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n")

print("=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

print("\n")

print("=" * 50)
print("Invalid Zero Values")
print("=" * 50)

columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in columns:
    print(f"{col}: {(df[col] == 0).sum()}")


plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.savefig("assets/age_distribution.png")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Outcome", data=df)

plt.title("Diabetes Outcome Distribution")

plt.savefig("assets/outcome_distribution.png")
plt.show()


plt.figure(figsize=(10,8))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("assets/correlation_heatmap.png")

plt.show()


