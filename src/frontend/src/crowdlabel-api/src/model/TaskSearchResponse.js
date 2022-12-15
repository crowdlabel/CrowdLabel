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
 * The TaskSearchResponse model module.
 * @module model/TaskSearchResponse
 * @version 0.1.0
 */
class TaskSearchResponse {
    /**
     * Constructs a new <code>TaskSearchResponse</code>.
     * @alias module:model/TaskSearchResponse
     * @param tasks {Array.<Number>} 
     * @param total {Number} 
     */
    constructor(tasks, total) { 
        
        TaskSearchResponse.initialize(this, tasks, total);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, tasks, total) { 
        obj['tasks'] = tasks;
        obj['total'] = total;
    }

    /**
     * Constructs a <code>TaskSearchResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TaskSearchResponse} obj Optional instance to populate.
     * @return {module:model/TaskSearchResponse} The populated <code>TaskSearchResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TaskSearchResponse();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('credits')) {
                obj['credits'] = ApiClient.convertToType(data['credits'], 'Number');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('requesters')) {
                obj['requesters'] = ApiClient.convertToType(data['requesters'], ['String']);
            }
            if (data.hasOwnProperty('page')) {
                obj['page'] = ApiClient.convertToType(data['page'], 'Number');
            }
            if (data.hasOwnProperty('credits_min')) {
                obj['credits_min'] = ApiClient.convertToType(data['credits_min'], 'Number');
            }
            if (data.hasOwnProperty('credits_max')) {
                obj['credits_max'] = ApiClient.convertToType(data['credits_max'], 'Number');
            }
            if (data.hasOwnProperty('sort_criteria')) {
                obj['sort_criteria'] = ApiClient.convertToType(data['sort_criteria'], 'String');
            }
            if (data.hasOwnProperty('sort_ascending')) {
                obj['sort_ascending'] = ApiClient.convertToType(data['sort_ascending'], 'Boolean');
            }
            if (data.hasOwnProperty('tasks')) {
                obj['tasks'] = ApiClient.convertToType(data['tasks'], ['Number']);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TaskSearchResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TaskSearchResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TaskSearchResponse.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tags'])) {
            throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['requesters'])) {
            throw new Error("Expected the field `requesters` to be an array in the JSON data but got " + data['requesters']);
        }
        // ensure the json data is a string
        if (data['sort_criteria'] && !(typeof data['sort_criteria'] === 'string' || data['sort_criteria'] instanceof String)) {
            throw new Error("Expected the field `sort_criteria` to be a primitive type in the JSON string but got " + data['sort_criteria']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tasks'])) {
            throw new Error("Expected the field `tasks` to be an array in the JSON data but got " + data['tasks']);
        }

        return true;
    }


}

TaskSearchResponse.RequiredProperties = ["tasks", "total"];

/**
 * @member {String} name
 */
TaskSearchResponse.prototype['name'] = undefined;

/**
 * @member {Number} credits
 */
TaskSearchResponse.prototype['credits'] = undefined;

/**
 * @member {Array.<String>} tags
 */
TaskSearchResponse.prototype['tags'] = undefined;

/**
 * @member {Array.<String>} requesters
 */
TaskSearchResponse.prototype['requesters'] = undefined;

/**
 * @member {Number} page
 */
TaskSearchResponse.prototype['page'] = undefined;

/**
 * @member {Number} credits_min
 */
TaskSearchResponse.prototype['credits_min'] = undefined;

/**
 * @member {Number} credits_max
 */
TaskSearchResponse.prototype['credits_max'] = undefined;

/**
 * @member {String} sort_criteria
 */
TaskSearchResponse.prototype['sort_criteria'] = undefined;

/**
 * @member {Boolean} sort_ascending
 */
TaskSearchResponse.prototype['sort_ascending'] = undefined;

/**
 * @member {Array.<Number>} tasks
 */
TaskSearchResponse.prototype['tasks'] = undefined;

/**
 * @member {Number} total
 */
TaskSearchResponse.prototype['total'] = undefined;






export default TaskSearchResponse;
