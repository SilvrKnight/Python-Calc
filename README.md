# Calculator Documentation

This documentation provides an overview of the calculator program.

## Functions

### `add(x, y)`

Adds two numbers.

**Parameters:**
- `x` (float or int): The first number.
- `y` (float or int): The second number.

**Returns:**
- float or int: The sum of `x` and `y`.

### `subtract(x, y)`

Subtracts two numbers.

**Parameters:**
- `x` (float or int): The first number.
- `y` (float or int): The second number.

**Returns:**
- float or int: The difference between `x` and `y`.

### `multiply(x, y)`

Multiplies two numbers.

**Parameters:**
- `x` (float or int): The first number.
- `y` (float or int): The second number.

**Returns:**
- float or int: The product of `x` and `y`.

### `divide(x, y)`

Divides two numbers.

**Parameters:**
- `x` (float or int): The numerator.
- `y` (float or int): The denominator.

**Returns:**
- float or int or None: The result of dividing `x` by `y`. If division by zero occurs, `None` is returned.

## Usage

To use the calculator program, follow these steps:

1. Select the desired operation from the main menu.
2. Enter the first number.
3. Enter the second number.
4. The result of the operation will be displayed.

Please note that numeric values must be entered, and the program handles both float and integer inputs. If an invalid input or division by zero occurs, appropriate error messages will be displayed.

## Example

```python
# Perform an addition operation
result = add(2, 3)
print(result)  # Output: 5

# Perform a division operation
result = divide(10, 2)
print(result)  # Output: 5.0
