from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


def train_model(df):

    df = df.dropna()

    # Encode categorical columns
    category_encoder = LabelEncoder()
    region_encoder = LabelEncoder()

    df['Category_encoded'] = category_encoder.fit_transform(df['Category'])
    df['Region_encoded'] = region_encoder.fit_transform(df['Region'])

    # Features
    X = df[['Category_encoded', 'Region_encoded']]

    # Target
    y = df['Sales']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, category_encoder, region_encoder