# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
click.disable_unicode_literals_warning = True


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
'''def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    
    N, instructions = parseFile(input)

    ledTester = LEDTester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('#occupied: ', ledTester.countOccupied()) 
    return 0


    def main(args=None):
    Console script for led_tester.
    click.echo("Replace this message by putting your code into "
               "led_tester.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0'''



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
