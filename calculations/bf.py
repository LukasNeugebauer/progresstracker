"""
Contains different equations to calculate body fat percentage
from circumference or caliper measurements or BMI
"""

"""
Using BMI to calculate body fat percentage
"""


def _bmi(weight, height):
    """
    Compute BMI from weight in kg and height in meters:
        weight / height^2
    Conversions from different metrics need to be done beforehand
    """
    return kg / m**2


def _bmi2bf(bmi, age, gender):
    """
    Uses a GLM to predict body fat percentage from BMI, age and gender.
    Gender has to be coded as 0 for women and 1 for men.
    Reference:
        Jackson, A., Stanforth, P., Gagnon, J. et al. The effect of sex, age
        and race on estimating percentage body fat from body mass index: The
        Heritage Family Study. Int J Obes 26, 789–796 (2002).
        https://doi.org/10.1038/sj.ijo.0802006
    """
    return (1.39 * bmi) + (0.16 * age) - (10.34 * gender) - 9


"""
Jackson & Pollock: Using skin fold measurements to directly estimate body fat
percentage without the need for conversion from average body density
Reference for all equations in this block:
    Jackson, A. S., & Pollock, M. L. (1985). Practical Assessment of Body
    Composition. The Physician and Sportsmedicine, 13(5), 76–90.
    doi:10.1080/00913847.1985.11708790
"""


"""
Jackson & Pollock: Using skin fold measurements to predict average body density
The results of these equations need to be converted to body fat using a
secondary equation.
Reference for equations for men:
Reference for equations for women:
"""

def _jp_bd_men_7(age, *args):
    """
    7-fold equation for men. Measurements are to be given in mm.
    Raises an error unless 7 measurements are given.
    """
    n_args = len(args)
    if not n_args == 7:
        raise ValueError(
            f"This equations needs 7 measurements, you gave only {n_args}."
        )
    sum_measurements = sum(args)
    return

"""
Secondary equations to convert average body density to body fat percentage
"""

def _brozek(density):
    """
    Compute body fat percentage from average body density according to Brozek's
    equation.
    Reference:
        Brozek J, Grande F, Anderson T, Keys A. Densitometric analysis of body
        composition: Revision of some quantitative assumptions.
        Ann N Y Acad Sci 1963; 26(110):113-40.
    """
    return (4.57 / density - 4.142) * 100


def _siri(density):
    """
    Compute body fat percentage from average body density according to Siri's
    equation.
    Reference:
        Siri WE. Body composition from fluid spaces and density: analyses of
        methods; in: Techniques for measuring body composition. Washington DC,
        Natl Acad. Sci. National Res. Council, 1961, pp. 223-244.
    """
    return (4.95 / density - 4.50) * 100


"""
Using skin fold caliper measurements to calculate average body density
"""


def _equ(*args):
    pass


"""
Using body circumference measurements to calculate average body density
as done by the U.S. Navy
"""


def _us_navy(gender, **kwargs):
    """
    Uses the US Navy approach to estimate body fat from height and
    circumference measurements. Note that there are different equations for
    men and women.
    Gender is assumed to be given as 1 for men and 0 for women
    Reference:
        Shake CL, Schlichting C, Mooney LW, Callahan AB, Cohen ME.
        Predicting percent body fat from circumference measurements.
        Mil Med. 1993 Jan;158(1):26-31. PMID: 8437737.
    """
    if gender == 0:
        return _us_navy_women(**kwargs)
    else:
        return _us_navy_men(**kwargs)


def _us_navy_men(height, neck, waist):
    return (
        495 / (1.0324 - 0.19077 * log10(waist - neck) +
        0.15456 * log10(height)) - 450
    )


def _us_navy_women(height, neck, waist, hip):
    return (
        495 / (1.29579 - 0.35004 * log10(waist + hip - neck) +
        0.22100 * log10(height)) - 450
    )
