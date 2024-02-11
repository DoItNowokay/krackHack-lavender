# CREATING BLOCKCHAIN FROM SCRATCH
# Organ Donation Website
This project is an organ donation website that facilitates the matching of donors and recipients, confirmation handling, digital signature creation, transaction creation and transparency, and blockchain integration for organ transplantation.

# Features
User Input: Users can input their details including personal information, blood group, and organ donation preferences.

Database Management: The system manages two databases, one for donors and another for recipients, storing their respective information securely.

Matching Algorithm: The system matches donors with compatible recipients based on various criteria such as blood type and organ compatibility.

Confirmation Handling: Once a match is found, the system sends confirmation notifications to both the donor and the recipient.

Digital Signature Creation: Upon confirmation, the system generates digital signatures for both the donor and the recipient to ensure the authenticity of the transaction.

Transaction Creation: After confirmation and signature generation, the system creates a transaction record detailing the organ donation process.

Validation and Blockchain Integration: The transaction record is validated for correctness and then added to the blockchain for secure and immutable storage.

Storage: The blockchain can be accessed and seen on cloud of MongoDB
# Installation
To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/organ-donation-website.git

Install dependencies:

cd krackHack-lavender

pip install -r requirements.txt.

Set up a MongoDB Atlas account:

Go to the MongoDB website and sign up for an account.

Create a new cluster and follow the setup instructions provided.

Whitelist your IP address to allow connections to your cluster.

Get your MongoDB connection URI:

Once your cluster is set up, click on "Connect" and choose "Connect your application".
Copy the connection string URI provided.
Set up environment variables:

# Replace placeholders with actual values
export DATABASE_URI="your_mongodb_connection_uri".

export DATABASE_PASSWORD="your_database_password".

Run the Flask server:

Usage
Access the website through your web browser at http://localhost:5000.

Fill in the required information in the provided forms.

Follow the on-screen instructions to complete the organ donation process.
# Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature).

Make your changes.

Commit your changes (git commit -am 'Add feature').

Push to the branch (git push origin feature).

Create a new Pull Request.
# License
This project is licensed under the MIT License - see the LICENSE file for details.
