/**
 * CrowdLabelAPI
 * API for CrowdLabel
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Point from './Point';

/**
 * The Corners model module.
 * @module model/Corners
 * @version 0.1.0
 */
class Corners {
    /**
     * Constructs a new <code>Corners</code>.
     * @alias module:model/Corners
     * @param topLeft {module:model/Point} 
     * @param bottomRight {module:model/Point} 
     */
    constructor(topLeft, bottomRight) { 
        
        Corners.initialize(this, topLeft, bottomRight);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, topLeft, bottomRight) { 
        obj['top_left'] = topLeft;
        obj['bottom_right'] = bottomRight;
    }

    /**
     * Constructs a <code>Corners</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Corners} obj Optional instance to populate.
     * @return {module:model/Corners} The populated <code>Corners</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Corners();

            if (data.hasOwnProperty('top_left')) {
                obj['top_left'] = Point.constructFromObject(data['top_left']);
            }
            if (data.hasOwnProperty('bottom_right')) {
                obj['bottom_right'] = Point.constructFromObject(data['bottom_right']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Corners</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Corners</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Corners.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `top_left`
        if (data['top_left']) { // data not null
          Point.validateJSON(data['top_left']);
        }
        // validate the optional field `bottom_right`
        if (data['bottom_right']) { // data not null
          Point.validateJSON(data['bottom_right']);
        }

        return true;
    }


}

Corners.RequiredProperties = ["top_left", "bottom_right"];

/**
 * @member {module:model/Point} top_left
 */
Corners.prototype['top_left'] = undefined;

/**
 * @member {module:model/Point} bottom_right
 */
Corners.prototype['bottom_right'] = undefined;






export default Corners;
