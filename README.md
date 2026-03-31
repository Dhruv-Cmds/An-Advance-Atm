# An Advance ATM

## Features
- User Authentication
- Balance Inquiry
- Cash Withdrawal
- Deposit Funds
- Transaction History

## Project Structure
```
An-Advance-Atm/
├── README.md
├── LICENSE
│
├── Advance_Atm/
│   ├── main.py
│   ├── atm.josn
│   ├── atm.txt
│
└── Advance_atm_Class/
    ├── main.py
    ├── atm.josn
    └── atm.txt
```

## Contributing
We welcome contributions! Please make sure to follow the guidelines:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Validation Rules
- User balance must not go below zero after withdrawal.
- All transactions must be logged for auditing purposes.