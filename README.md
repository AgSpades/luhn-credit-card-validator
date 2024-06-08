# Credit Card Validator

This python3 program validates credit card numbers using the Luhn algorithm. It verifies the checksum and correct digit sequence, ensuring that the input is a valid 16-digit credit card number. This project is part of my collection of simple [validation projects](https://github.com/AgSpades/validation-projects) using Python.

## Features

- Validates credit card numbers using the Luhn algorithm
- Ensures the credit card number is exactly 16 digits long
- Handles incorrect inputs gracefully

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `cc-validator.py` script.
2. Run the script using python3:

    ```sh
    python3 cc-validator.py
    ```

3. Enter a 16-digit credit card number when prompted.

## Example

```sh
$ python3 cc-validator.py
Enter credit card number: 371449635398431
Valid credit card number.
```
## How It Works

1. Input Validation: The program first checks if the input is a string of 16 digits.
2. Luhn Algorithm: It then processes the digits using the Luhn algorithm to determine if the number is valid.
3. Checksum Calculation: The Luhn algorithm calculates a checksum by:
    - Doubling every second digit from the right.
    - Summing the digits of the products and the undoubled digits.
    - Checking if the total modulo 10 is 0.

## License

This project is licensed under the [MIT License](./LICENSE) - see the LICENSE file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## Acknowledgements

- The Luhn algorithm was developed by [Hans Peter Luhn](https://en.wikipedia.org/wiki/Hans_Peter_Luhn), a scientist at IBM.