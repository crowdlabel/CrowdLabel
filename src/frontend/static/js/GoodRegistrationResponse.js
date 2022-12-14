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

/**
 * The GoodRegistrationResponse model module.
 * @module model/GoodRegistrationResponse
 * @version 0.1.0
 */
class GoodRegistrationResponse {
    /**
     * Constructs a new <code>GoodRegistrationResponse</code>.
     * @alias module:model/GoodRegistrationResponse
     * @param username {String} 
     * @param email {String} 
     * @param userType {String} 
     */
    constructor(username, email, userType) { 
        
        GoodRegistrationResponse.initialize(this, username, email, userType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, username, email, userType) { 
        obj['username'] = username;
        obj['email'] = email;
        obj['user_type'] = userType;
    }

    /**
     * Constructs a <code>GoodRegistrationResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GoodRegistrationResponse} obj Optional instance to populate.
     * @return {module:model/GoodRegistrationResponse} The populated <code>GoodRegistrationResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GoodRegistrationResponse();

            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('user_type')) {
                obj['user_type'] = ApiClient.convertToType(data['user_type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GoodRegistrationResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GoodRegistrationResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GoodRegistrationResponse.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['user_type'] && !(typeof data['user_type'] === 'string' || data['user_type'] instanceof String)) {
            throw new Error("Expected the field `user_type` to be a primitive type in the JSON string but got " + data['user_type']);
        }

        return true;
    }


}

GoodRegistrationResponse.RequiredProperties = ["username", "email", "user_type"];

/**
 * @member {String} username
 */
GoodRegistrationResponse.prototype['username'] = undefined;

/**
 * @member {String} email
 */
GoodRegistrationResponse.prototype['email'] = undefined;

/**
 * @member {String} user_type
 */
GoodRegistrationResponse.prototype['user_type'] = undefined;






export default GoodRegistrationResponse;

