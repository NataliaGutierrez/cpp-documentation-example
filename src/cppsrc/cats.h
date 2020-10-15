#pragma once

/** @addtogroup cat */
/*@{*/

/**
	A fluffy feline
*/
struct cat {
  /** Evaluate if a location in metric space falls inside the element.
   *  This method evaluates if a location is inside the element, and if it
   *  does, returns coordinates in the element stored in a topologic point.
   *  This method must be implmented in subclasses, and is aimed to be
   *  used in reference system transformations from mesh classes.
   *  @param [in] point     input coordinates
   *  @param [in] elem      element id
   *  @param [in] nodelist  List of existing nodes
   *  @return tuple {inside_flag, point in new coordinates}
   */
	void make_cute();
};

/*@}*/
